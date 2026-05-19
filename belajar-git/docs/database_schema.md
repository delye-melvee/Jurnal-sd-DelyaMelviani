# Database Schema

## Tabel Users
Digunakan untuk menyimpan data pengguna aplikasi.

Kolom:
- id
- username
- email
- password
- avatar_url

## Tabel Login_History
Digunakan untuk menyimpan riwayat login pengguna.

Kolom:
- id
- user_id
- login_time
- ip_address