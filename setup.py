from setuptools import setup
import os, shutil, platform
from setuptools.command.install import install

class custom_install_command(install):
    def run(self):
        install.run(self)
        target_dir = os.path.join(self.install_lib, "ten_vad_library")
        os.makedirs(target_dir, exist_ok=True)
        
        # Copy libraries for all platforms
        lib_files = []
        
        # Linux library
        linux_lib_path = "lib/Linux/x64/libten_vad.so"
        if os.path.exists(linux_lib_path):
            lib_files.append((linux_lib_path, os.path.join(target_dir, "libten_vad.so")))
            print(f"Found Linux library: {linux_lib_path}")
            
        # Windows library
        windows_lib_path = "lib/Windows/x64/ten_vad.dll"
        if os.path.exists(windows_lib_path):
            lib_files.append((windows_lib_path, os.path.join(target_dir, "ten_vad.dll")))
            print(f"Found Windows library: {windows_lib_path}")
            
        # macOS library
        macos_lib_path = "lib/macOS/x64/libten_vad.dylib"
        if os.path.exists(macos_lib_path):
            lib_files.append((macos_lib_path, os.path.join(target_dir, "libten_vad.dylib")))
            print(f"Found macOS library: {macos_lib_path}")
            
        # Copy all found libraries to the target directory
        for src, dst in lib_files:
            shutil.copy(src, dst)
            print(f"Copied {src} to {dst}")
            
        print(f"Libraries installed to: {target_dir}")
        
        # Also create a platform-specific symbolic link or copy for easier access
        current_platform = platform.system().lower()
        if current_platform == "windows":
            for src, dst in lib_files:
                if "windows" in src.lower():
                    print(f"Current platform is Windows, using {os.path.basename(dst)}")
                    break
        elif current_platform == "darwin":  # macOS
            for src, dst in lib_files:
                if "macos" in src.lower():
                    print(f"Current platform is macOS, using {os.path.basename(dst)}")
                    break
        else:  # Linux and others
            for src, dst in lib_files:
                if "linux" in src.lower():
                    print(f"Current platform is Linux, using {os.path.basename(dst)}")
                    break

# Simple setup function - pyproject.toml handles most metadata now
setup(
    cmdclass={
        "install": custom_install_command,
    },
)