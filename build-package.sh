PROJECT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
echo "Project dir is $PROJECT_DIR"

# Load build number & version number from file
export BUILD_NUMBER=$(cat BUILD_NUMBER)
export VERSION_NUMBER=$(cat VERSION_NUMBER)

# Increment the build number for each build
export BUILD_NUMBER=$(($BUILD_NUMBER+1))
echo "$BUILD_NUMBER" > $PROJECT_DIR/BUILD_NUMBER

# Trigger conda build process
conda build $PROJECT_DIR