#!/bin/bash

# Get game number
g=$1

# Get project path
proj=$(pwd)

function showExampleUse {
	echo "# Use example: bash testExamples.sh <X>"
	echo "# Posibles <X>: 1 2 3 4 5 6 10 15 20 30 ..."
}

if [ $# -ne 1 ]
then
	echo -e "[ERROR 404] No game number found\n"
	showExampleUse
	exit 1
fi

re="^[0-9]+$"
if ! [[ $g =~ $re ]]
then
	echo -e "[ERROR 505] Argument must be the number of the game\n"
	showExampleUse
	exit 1
fi

g=$(printf "%03d" ${g})

pathFolder=($(ls ${proj} | grep G${g}))
if ! [[ $pathFolder ]]
then
	echo -e "[ERROR 404] Folder for game ${g} not found"
	exit 1
elif [[ ${#pathFolder[@]} -ne 1 ]]
then
	echo -e "[ERROR 505] Found more than 1 folder for game ${g}"
	exit 1
fi

echo "[INFO] Executing examples for game ${g}"
echo "[INFO] Folder ${pathFolder}"

pathExamples=($(ls ${pathFolder} | grep -w Examples))
if ! [[  $pathExamples ]]
then
	echo -e "[ERROR 404] Folder 'Examples' not found for game ${g}"
	exit 1
fi

echo "[INFO] Iterating over all examples in $pathExamples folder"
allExamples=($(ls "${pathFolder}/Examples" | grep example))
for (( nex=0; nex<=${#allExamples[@]}; nex++))
do
	filex="example${nex}.txt"
	solex="solutionExample${nex}.txt"
	
	echo -e "[INFO] File ${filex}\n[INFO] File ${solex}\nResult:"
	python ${pathFolder}/code${g}.py "${pathFolder}/Examples/${filex}"
	echo -e "Solution:"
	cat "${pathFolder}/Examples/${solex}"
done


# Use example: bash testExamples.sh <X>
# Posibles <X>: 1 2 3 4 5 6 10 15 20 30 ...
