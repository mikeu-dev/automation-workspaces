# n8n Automation Workspaces

[English](./README.md) 🇬🇧

Selamat datang di repositori pusat pengelolaan alur kerja otomatisasi (**automation workflows**) berbasis **n8n**. Repositori ini dirancang dengan struktur multi-workspace untuk mempermudah manajemen, pelacakan versi, dan kolaborasi dalam pengembangan sistem otomatisasi bisnis.

---

## Struktur Repositori

Repositori ini menggunakan struktur monorepo sederhana berbasis workspace untuk mengisolasi setiap proyek otomatisasi beserta dependensinya (seperti konfigurasi Docker Compose, volume data, dan berkas ekspor alur kerja).

```bash
.
├── .gitignore
├── README.md               # Dokumentasi utama repositori (Bahasa Inggris)
├── README.id.md            # Dokumentasi repositori (Bahasa Indonesia)
└── workspaces/             # Direktori proyek otomatisasi
    └── blog-content-engine/   # Engine pembuatan konten blog otomatis B2B
```

---

## Daftar Workspaces

Saat ini, repositori ini mengelola workspace aktif berikut:

| Workspace | Versi | Komponen Utama | Deskripsi Singkat |
| :--- | :---: | :--- | :--- |
| [**Blog Content Engine**](workspaces/blog-content-engine/README.id.md) | `v3.3.1` | n8n, Qdrant, Google Gemini | Pembangkit artikel blog B2B berbasis SEO yang didukung oleh teknologi RAG (Retrieval-Augmented Generation) untuk menjamin akurasi konten berdasarkan basis pengetahuan riil. |

---

## Prasyarat Umum

Untuk menjalankan alur kerja di dalam repositori ini, pastikan sistem Anda telah terpasang:
*   [Docker](https://docs.docker.com/get-docker/) (Versi 20.10+)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Versi 2.0+)
*   Koneksi internet aktif untuk penarikan citra (*image*) Docker dan akses API eksternal (seperti Google Gemini API).

---

## Cara Memulai

Untuk mulai menggunakan salah satu workspace:

1.  **Kloning Repositori**:
    ```bash
    git clone <url-repositori-ini> n8n-automation
    cd n8n-automation
    ```

2.  **Pilih & Jalankan Proyek**:
    Masuk ke direktori workspace pilihan Anda, lalu jalankan layanannya. Sebagai contoh untuk `blog-content-engine`:
    ```bash
    cd workspaces/blog-content-engine
    docker compose up -d
    ```

3.  **Akses n8n**:
    Buka peramban (*browser*) Anda dan akses dashboard n8n di: `http://localhost:5678`

4.  **Impor Alur Kerja**:
    Ekspor alur kerja berupa file JSON (seperti `core.json`) dapat diimpor langsung ke dashboard n8n Anda.

---

## Kebijakan Kontribusi & Git

*   **Pola Commit**: Repositori ini menerapkan standar [Conventional Commits](https://www.conventionalcommits.org/). Setiap pesan commit wajib ditulis dalam **bahasa Inggris** dengan format teratur:
    *   `feat: <deskripsi>` untuk fitur baru.
    *   `fix: <deskripsi>` untuk perbaikan bug.
    *   `docs: <deskripsi>` untuk pembaruan dokumentasi.
*   **Penandaan Versi (Tagging)**: Karena repositori ini menggunakan arsitektur monorepo dengan berbagai *workspace*, penandaan versi wajib menggunakan **Scoped Tagging** agar versi setiap *workspace* dapat dikelola secara independen:
    *   Format: `<nama-workspace>@v<versi>` (Contoh: `blog-content-engine@v3.3.1`)
*   **Keamanan Kredensial**: **Dilarang keras** men-commit file `.env` berisi kunci API sensitif atau kredensial produksi. Gunakan template `.env.example` jika diperlukan.

---
Dokumentasi ini dikelola oleh mikeu-dev.
