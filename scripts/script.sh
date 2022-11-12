#!/bin/bash

#\Users\Titan\Desktop\Projects\Python\Python\scripts\script.sh >> \Users\Titan\Desktop\Projects\Python\Python\scripts\script.out 2>&1
exec >logfile.out 2>&1
echo "Begin execution"
python main.py
echo "End of execution"
