
## 📥 Sovereign Installation (Termux/Android)

To instantiate the Atmos Atlas-01 on a mobile node, follow this high-fidelity path:

### Step 1: Substrate Preparation
Ensure your environment has the necessary build tools and Java runtime.
```bash
pkg update && pkg upgrade
pkg install git python openjdk-17 gradle binutils rust cmake

cd ~/Atmos-Atlas-01/android
gradle wrapper
chmod +x gradlew

./gradlew assembleRelease

termux-open app/build/outputs/apk/release/app-release.apk

