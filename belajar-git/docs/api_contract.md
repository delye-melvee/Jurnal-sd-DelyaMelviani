# API Contract - User Profile

**Endpoint:** `/api/v1/profile`
---

# API Contract - Login

**Endpoint:** `/api/v1/login`

**Method:** `POST`

**Request Body (JSON):**

```json
{
  "email": "user@email.com",
  "password": "123456"
}
```

**Response Body (JSON):**

```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "abc123xyz"
}
```

**Method:** `GET`

**Response Body (JSON):**

```json
{
  "id": 1,
  "username": "mahasiswa_sd",
  "email": "mhs@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```