cd ~/Atmos

# 1. Final verification of the structure
# Ensure all new directories are recognized
git add .

# 2. Execute the Ghost Commit for this synchronization
# This strips your local identity from the push metadata
git commit --author="Sovereign-Operator <void@atmos.mesh>" \
-m "ATMOS CORE v3.1: UNITARY 2.0 - CI/CD FORGE INITIALIZATION"

# 3. Synchronize with the Remote Forge
# Using --force ensures the remote history matches our ghosted local history
git push origin main --force

# 4. Trigger the Build Engine
# This creates the 'v3.1.0' tag, which signals GitHub Actions to build the APK
git tag -a v3.1.0 -m "Release v3.1.0 - Unitary Logic"
git push origin v3.1.0


