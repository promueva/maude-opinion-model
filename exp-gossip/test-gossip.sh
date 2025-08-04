#!/bin/bash

# ulimit -v 304087040
# Varying the number of iterations to reach consensus 

# Path to your file
INPUT_FILE="./formulaG.quatex"
TEMP_FILE="./formula.quatex"
OUTPUT="./results.csv"

INI=10
END=600
STEP=10

AINI=2
AEND=50
ASTEP=1

echo "agents;comms;simulations;mean;dvest;r;time" >> $OUTPUT 

for AN in $(seq $AINI $ASTEP $AEND); do
    echo "Running with AGENTS = $AN"
    python ./generate-gossip.py --agents $AN > model.maude
    cp model.maude files/$AN.maude

    for N in $(seq $INI $STEP $END); do
        # Replace the N in the formula
        sed "s/eval E\[Prob *(PARAM) *\]/eval E[Prob ($N)]/" "$INPUT_FILE" > "$TEMP_FILE"

        echo "Running with N = $N"
        output=$( { /usr/bin/time -f "Time: %E" umaudemc scheck model.maude init formula.quatex -a 0.05 -d 0.02  --jobs 16 --assign metadata ; } 2>&1 )

        simulations=$(echo "$output" | grep -Po 'Number of simulations = \K[0-9]+')
        mu=$(echo "$output" | grep -Po 'μ = \K[0-9.]+')
        sigma=$(echo "$output" | grep -Po 'σ = \K[0-9.]+')
        r=$(echo "$output" | grep -Po 'r = \K[0-9.]+')
        time=$(echo "$output" | grep -Po 'Time: \K[0-9:.]+')
        
        csv="${AN};${N};${simulations};${mu};${sigma};${r};${time}"


        echo $output
        echo "$csv" >> $OUTPUT 
    done
done
