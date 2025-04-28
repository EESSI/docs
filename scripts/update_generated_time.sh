#!/usr/bin/env bash

# Default values
section=""
file=""

# Print help message
print_help() {
    echo "Usage: $0 --section SECTION --file FILE"
    echo
    echo Updates the timestamp for the automatically generated docs for the section SECTION in the file FILE
    echo
    echo "Valid sections:"
    echo "  available_software   -> Updates 'generated_time (available software)' field in FILE"
    echo "  testsuite_api         -> Updates 'generated_time (EESSI testsuite API docs)' field in FILE"
    echo
    exit 0
}

# Parse named options
while [[ $# -gt 0 ]]; do
    case "$1" in
        --section)
            section="$2"
            shift 2
            ;;
        --file)
            file="$2"
            shift 2
            ;;
        --help)
            print_help
            ;;
        *)
            echo "Unknown option: $1"
            print_help
            exit 1
            ;;
    esac
done

# Validate section
if [[ -z "$section" ]]; then
    echo "ERROR: --section argument is required."
    print_help
    exit 1
fi

# Validate file
if [[ -z "$file" ]]; then
    echo "ERROR: --file argument is required."
    print_help
    exit 1
fi

# Get the new date
NEW_DATE="$(date '+%a, %d %b %Y at %H:%M:%S %Z')"

# Replace date for requested section
case "$section" in
    available_software)
        sed -E -i 's/(generated_time \(available software\): ")[^"]*(".*)/\1'"${NEW_DATE}"'\2/' $file
        ;;
    testsuite_api)
        sed -E -i 's/(generated_time \(testsuite API\): ")[^"]*(".*)/\1'"${NEW_DATE}"'\2/' $file
        ;;
    *)
        echo "ERROR: Unknown section '$section'"
        echo "Valid sections are: available_software, testsuite_api"
        exit 1
        ;;
esac
