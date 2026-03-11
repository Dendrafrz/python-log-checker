# 🔐 SSH Log Analyzer

Script Python sederhana untuk mendeteksi **failed login attempts** dari file `auth.log` Linux. Cocok untuk monitoring keamanan server secara manual.

---

## 📋 Requirements

- Python 3.6+
- Tidak butuh library eksternal (hanya `os` bawaan Python)

---

## 🚀 Cara Pakai

### 1. Clone / Download script

```bash
git clone https://github.com/username/ssh-log-analyzer.git
cd ssh-log-analyzer
```

### 2. Siapkan file log

Salin `auth.log` dari server ke direktori yang sama dengan script:

```bash
# Langsung dari server Linux
sudo cp /var/log/auth.log .

# Atau dari remote server via SCP
scp user@server:/var/log/auth.log .
```

### 3. Jalankan script

```bash
python analyze_log.py
```

---

## 📤 Contoh Output

```
[*] Menganalisis 1024 row log...
[!] failed: Dec 10 03:21:44 server sshd[12345]: Failed password for root from 192.168.1.10 port 54321 ssh2
[!] failed: Dec 10 03:21:47 server sshd[12346]: Failed password for admin from 192.168.1.10 port 54322 ssh2
[!] failed: Dec 10 03:21:50 server sshd[12347]: Failed password for invalid user test from 10.0.0.5 port 43210 ssh2
```

---

## 📁 Struktur File

```
ssh-log-analyzer/
├── analyze_log.py   # Script utama
├── auth.log         # File log (tidak di-commit ke repo)
└── README.md
```

> ⚠️ **Jangan commit `auth.log`** ke GitHub karena bisa mengandung informasi sensitif. Tambahkan ke `.gitignore`:
> ```
> auth.log
> *.log
> ```

---

## 🗺️ Planned Features

- [ ] Filter hasil berdasarkan IP address tertentu
- [ ] Hitung jumlah percobaan gagal per user / per IP
- [ ] Deteksi potensi brute force (threshold attempts)
- [ ] Export hasil ke CSV
- [ ] Support format log selain `auth.log` (misal: `syslog`, `secure`)
- [ ] Argumen CLI (`--file`, `--output`, `--threshold`)

---

## ⚠️ Disclaimer

Script ini dibuat untuk keperluan **monitoring dan audit keamanan sistem sendiri**. Jangan digunakan untuk menganalisis log sistem yang bukan milik kamu tanpa izin.

---

## 📄 License

MIT License
