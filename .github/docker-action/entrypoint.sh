#!/bin/sh -l
export PYTHONSTARTUP=/app/.pythonrc
sh -c ls -la /app
for module in common data game login ; do \
		cd $module; \
		pip install -r requirements.txt; \
		cd ..; \
done
black --check . -v --target-version py310
isort --profile=black . --check-only
echo "Hello"
time=$(date)
echo "::set-output name=time::$time"