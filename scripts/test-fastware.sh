#!/bin/bash
# FastWare Test Runner

echo "Running FastWare Tests..."
echo "------------------------"

# Run unit tests
python3 -m unittest discover fastware/tests

if [ $? -eq 0 ]; then
    echo "------------------------"
    echo "All FastWare tests PASSED!"
    exit 0
else
    echo "------------------------"
    echo "Some FastWare tests FAILED!"
    exit 1
fi
