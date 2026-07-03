import os

user_name = os.getenv('APP_USER', 'Guest')
app_env = os.getenv('APP_ENV', 'Development')

if __name__ == "__main__":
    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
    print(f"Status Lingkungan: {app_env}")
    print("Versi 2.0 - Stabil")