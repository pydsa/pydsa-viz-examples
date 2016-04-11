#!/usr/bin/env python

echo "HELLO! THIS PYTHON ALGORITHM EXECUTOR"
echo "AVAILABLE ALGORITHM IMPLEMENTATIONS ARE:"
echo
echo "1. LINE INTERSECTION WITH VISUALIZATION"
echo "2. QUICKSORT WITH VISUALIZATION"
echo
echo "Enter your choice (1/2):"
read inp
if [ "$inp" -eq 1 ]; then
    echo "Executing Line intersection"
    echo
    echo
    chmod +x line.py
    python line.py
elif [ "$inp" -eq 2 ]; then
    echo "Executing Quicksort"
    echo 
    echo
    chmod +x sort.py
    python sort.py
else
    echo
    echo "WRONG CHOICE!!"
fi

echo
echo "Done"
    
