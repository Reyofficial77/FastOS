PROJECT: FastOS — Lightweight Linux Desktop Operating System



Kamu bertindak sebagai Senior Linux Distribution Engineer, Linux System Administrator, Desktop Environment Developer, UI/UX Designer, dan Build \& Release Engineer.



Tugasmu adalah membangun sebuah sistem operasi Linux sungguhan bernama FastOS yang dapat di-boot dan digunakan langsung melalui VirtualBox.



Ini bukan proyek website, simulasi OS, dashboard web, atau sekadar desktop mockup. Hasil akhirnya harus berupa distribusi Linux yang benar-benar dapat dijalankan.



Jangan hanya membuat dokumentasi, rencana, atau contoh kode. Implementasikan proyek secara bertahap, uji hasilnya, perbaiki error, dan siapkan proses build ISO yang bisa diulang.



\---



1\. VISI FASTOS



Nama: FastOS

Codename: Swift

Kategori: Lightweight Linux Desktop Distribution

Base OS: Debian Stable minimal installation

Arsitektur awal: x86\_64 / AMD64

Target pertama: VirtualBox

Target berikutnya: PC dan laptop x86\_64

Bahasa antarmuka awal: Bahasa Inggris, dengan dukungan Bahasa Indonesia

Lisensi: Gunakan komponen open-source dengan lisensi yang sesuai.



FastOS adalah sistem operasi desktop Linux yang menggabungkan:



\- Kesederhanaan dan kompatibilitas aplikasi Linux.

\- Produktivitas dan kemudahan penggunaan Windows.

\- Estetika minimalis, konsisten, dan elegan seperti macOS.

\- Konsumsi RAM dan CPU serendah mungkin tanpa mengorbankan kestabilan.

\- Pengalaman instalasi dan penggunaan yang mudah bagi pengguna baru.



Gunakan teknologi Linux yang benar-benar ada. Jangan membuat komponen palsu hanya demi tampilan.



2\. ARSITEKTUR SISTEM



Gunakan fondasi berikut:



\- Debian Stable sebagai base distribution.

\- Linux kernel resmi dari repositori Debian.

\- systemd untuk init dan manajemen service.

\- XFCE sebagai desktop environment dasar karena ringan dan matang.

\- LightDM sebagai display manager.

\- Xorg sebagai pilihan awal yang kompatibel dengan VirtualBox.

\- NetworkManager untuk koneksi jaringan.

\- PipeWire dan WirePlumber untuk audio jika kompatibel dengan konfigurasi yang dipilih.

\- UEFI dan BIOS legacy jika didukung oleh metode build.

\- GRUB sebagai bootloader untuk instalasi pada disk.

\- live-build atau pendekatan resmi Debian lain yang sesuai untuk membangun ISO.

\- Calamares sebagai graphical installer jika kompatibilitas dan integrasinya memungkinkan.



Jangan mengganti teknologi hanya karena namanya terdengar lebih modern. Pilih berdasarkan stabilitas, kompatibilitas, ukuran, dan konsumsi resource.



Gunakan repositori resmi dan paket yang masih didukung. Jangan menambahkan repositori tidak tepercaya tanpa alasan teknis yang jelas.



Dokumentasikan semua keputusan arsitektur yang penting.



3\. TARGET PERFORMA



FastOS harus dirancang agar ringan ketika idle.



Target pengujian awal pada VirtualBox:



\- RAM VM: 2 GB dan 4 GB.

\- CPU VM: 2 virtual CPU.

\- Penyimpanan virtual: 20 GB.

\- Grafik virtual: VMSVGA.

\- Target idle RAM: sekitar 500–800 MB jika realistis.

\- Target CPU idle: mendekati 0–5% pada VM yang sedang tidak melakukan pekerjaan.

\- Desktop harus tetap responsif saat membuka menu, file manager, terminal, dan aplikasi.

\- Waktu boot harus diukur dan dioptimalkan.

\- Service yang tidak diperlukan tidak boleh dijalankan tanpa alasan.



Angka di atas adalah sasaran pengembangan, bukan klaim yang boleh dibuat tanpa pengukuran.



CPU usage di bawah 5% bukan jaminan konstan. Beban sistem bergantung pada hardware, driver, proses latar belakang, resolusi layar, dan aktivitas pengguna.



Buat benchmark yang mencatat:



1\. Penggunaan RAM setelah boot dan login.

2\. CPU usage saat idle selama 60 detik.

3\. Waktu dari boot hingga desktop siap.

4\. Penggunaan disk setelah instalasi.

5\. Jumlah service aktif.

6\. Waktu membuka aplikasi utama.



Sediakan skrip benchmark, misalnya:



scripts/benchmark.sh



Gunakan alat seperti free, vmstat, ps, systemd-analyze, dan /proc/meminfo jika sesuai.



Jangan menonaktifkan service penting, keamanan, logging, jaringan, atau pengelolaan daya hanya demi mengejar angka rendah.



4\. DESAIN DESKTOP FASTOS



Buat identitas visual FastOS sendiri. Jangan menyalin aset berhak cipta dari Windows atau macOS.



Gaya visual:



\- Modern, minimalis, elegan.

\- Perpaduan konsep Windows dan macOS.

\- Dark mode sebagai tema default.

\- Light mode sebagai alternatif.

\- Aksen biru dengan gradasi halus.

\- Ikon konsisten dan mudah dikenali.

\- Animasi singkat dan ringan.

\- Sudut jendela sedikit membulat.

\- Tipografi yang mudah dibaca.

\- Tidak menggunakan efek blur atau transparansi berlebihan yang membebani GPU.



Desktop layout



Buat layout desktop dengan:



1\. Panel atas tipis berisi:

&#x20;  

&#x20;  - Logo FastOS.

&#x20;  - Menu aplikasi.

&#x20;  - Informasi tanggal dan jam.

&#x20;  - Status jaringan.

&#x20;  - Volume.

&#x20;  - Baterai jika perangkat mendukung.

&#x20;  - Menu sesi dan daya.



2\. Dock bawah:

&#x20;  

&#x20;  - File Manager.

&#x20;  - Browser.

&#x20;  - FastWare.

&#x20;  - Terminal.

&#x20;  - Settings.

&#x20;  - Text Editor.

&#x20;  - Trash.



3\. Desktop:

&#x20;  

&#x20;  - Wallpaper resmi FastOS.

&#x20;  - Ikon desktop opsional.

&#x20;  - Klik kanan untuk menu konteks.

&#x20;  - Pintasan yang berguna.



4\. Window management:

&#x20;  

&#x20;  - Minimize, maximize, close.

&#x20;  - Alt+Tab untuk berpindah aplikasi.

&#x20;  - Workspace virtual.

&#x20;  - Shortcut keyboard yang masuk akal.

&#x20;  - Panel dan dock tidak boleh saling bertumpuk.



Gunakan XFCE panel, dock ringan yang kompatibel, tema GTK, ikon, dan konfigurasi window manager yang sudah tersedia jika memungkinkan.



Jangan membuat seluruh desktop sebagai aplikasi web atau Electron.



Jika suatu fitur harus dibuat sendiri, gunakan teknologi desktop Linux yang sesuai, misalnya Python GTK, C, atau teknologi native lain yang memang diperlukan.



Prioritaskan penggunaan resource rendah.



5\. FASTWARE — SOFTWARE CENTER BAWAAN



Buat aplikasi desktop native bernama FastWare.



FastWare adalah pusat instalasi aplikasi resmi FastOS. Pengguna harus bisa membuka FastWare dari dock atau menu aplikasi.



FastWare bukan halaman web yang berpura-pura menjadi software installer.



Fitur wajib



\- Halaman Home.

\- Kategori aplikasi.

\- Pencarian aplikasi.

\- Detail aplikasi.

\- Tombol Install.

\- Progress instalasi.

\- Tombol Cancel jika operasi memungkinkan untuk dibatalkan dengan aman.

\- Tombol Open setelah aplikasi terpasang.

\- Tombol Uninstall.

\- Daftar aplikasi terpasang.

\- Pesan error yang mudah dipahami.

\- Indikator loading dan status operasi.

\- Deteksi apakah aplikasi sudah terpasang.



Kategori aplikasi:



\- Development.

\- Multimedia.

\- Internet.

\- Office.

\- Graphics.

\- Utilities.

\- System Tools.

\- Games.



Aplikasi awal yang perlu dipertimbangkan:



\- Visual Studio Code.

\- OBS Studio.

\- Firefox.

\- Chromium.

\- VLC.

\- GIMP.

\- LibreOffice.

\- Audacity.

\- Git.

\- Python.

\- Blender.

\- Inkscape.

\- FileZilla.

\- Telegram Desktop jika paket yang tepercaya tersedia.



Jangan menganggap semua aplikasi harus tersedia di repositori Debian. Periksa ketersediaan, arsitektur, lisensi, dan sumber resmi setiap aplikasi.



Sumber paket



Gunakan urutan prioritas:



1\. Repositori resmi Debian.

2\. Flatpak melalui Flathub jika diperlukan dan telah dikonfigurasi dengan benar.

3\. Sumber resmi vendor jika distribusi dan lisensinya mengizinkan.



Untuk Visual Studio Code, gunakan paket atau repositori resmi Microsoft jika dibutuhkan dan tersedia secara aman. Jangan menyebut Code - OSS sebagai produk identik dengan Visual Studio Code tanpa menjelaskan perbedaannya.



OBS Studio harus menggunakan sumber paket yang kompatibel dengan versi Debian yang dipilih.



Jangan menjalankan perintah instalasi yang berasal dari input pengguna tanpa validasi.



Keamanan FastWare



\- Jangan menjalankan seluruh aplikasi FastWare sebagai root.

\- Gunakan PolicyKit atau mekanisme otorisasi sistem yang sesuai.

\- Tampilkan permintaan autentikasi saat operasi administratif diperlukan.

\- Jangan menyimpan password pengguna.

\- Jangan menggunakan sudo tanpa pembatasan.

\- Jangan membuat endpoint shell arbitrer.

\- Validasi ID paket menggunakan katalog yang telah ditentukan.

\- Gunakan proses subprocess dengan argumen terpisah, bukan perintah shell hasil penggabungan string.

\- Tampilkan status proses dan tangani error.

\- Cegah dua operasi paket yang saling bertentangan berjalan bersamaan.

\- Jangan menghapus paket inti yang diperlukan FastOS.



Jika Flatpak dipakai, jelaskan bahwa aplikasi Flatpak bisa menambah penggunaan disk dan RAM. Jangan menjanjikan semua aplikasi akan berjalan dengan resource rendah yang sama.



Implementasi



Gunakan Python dengan GTK 3 atau GTK 4, mengikuti kompatibilitas library dan desktop yang dipilih.



Pisahkan kode menjadi beberapa modul yang jelas, misalnya:



fastware/

app.py

ui/

services/

catalog/

package\_manager/

security/

tests/



Struktur akhir boleh disesuaikan berdasarkan kebutuhan nyata.



Buat katalog aplikasi dalam format data yang mudah dipelihara. Jangan mengandalkan scraping website.



FastWare harus tetap bisa dibuka ketika jaringan tidak tersedia, setidaknya untuk menampilkan katalog lokal, status aplikasi, dan informasi error.



6\. FILE MANAGER DAN APLIKASI BAWAAN



Pilih aplikasi yang ringan dan matang.



Minimal:



\- File manager.

\- Terminal emulator.

\- Text editor.

\- Browser.

\- Archive manager.

\- Image viewer.

\- Settings manager.

\- System monitor.

\- Screenshot tool.

\- Audio control.

\- Network manager UI.



Jangan mengganti aplikasi sistem yang sudah berfungsi tanpa alasan kuat.



Sediakan pintasan keyboard dasar dan integrasikan aplikasi ke menu desktop.



7\. FASTOS SETTINGS



Buat pusat pengaturan desktop yang mudah digunakan.



Pengaturan minimal:



\- Appearance.

\- Dark/Light Mode.

\- Wallpaper.

\- Display Resolution.

\- Keyboard.

\- Mouse dan touchpad.

\- Network.

\- Sound.

\- Power.

\- Startup Applications.

\- Language.

\- Date and Time.

\- Users dan sesi.

\- About FastOS.



Manfaatkan panel pengaturan XFCE yang sudah tersedia. Buat pembungkus atau modul native tambahan hanya jika memang diperlukan.



Pengaturan harus benar-benar mengubah konfigurasi sistem. Jangan membuat tombol yang hanya mengubah tampilan tanpa melakukan tindakan nyata.



8\. INSTALLER DAN FIRST BOOT



FastOS harus menyediakan proses instalasi yang mudah bagi pemula.



Target alur:



1\. Boot ISO FastOS.

2\. Masuk ke live desktop jika didukung.

3\. Pengguna membuka installer.

4\. Memilih bahasa.

5\. Memilih zona waktu.

6\. Memilih keyboard.

7\. Menyiapkan disk virtual.

8\. Membuat akun pengguna.

9\. Menentukan password.

10\. Mengonfirmasi instalasi.

11\. Sistem memasang paket.

12\. Bootloader dikonfigurasi.

13\. Instalasi selesai.

14\. Pengguna melakukan reboot.

15\. FastOS masuk ke desktop yang telah diinstal.



Untuk tahap awal, prioritaskan instalasi ke disk virtual kosong.



Jangan melakukan format otomatis pada disk yang sudah berisi data. Selalu tampilkan ringkasan partisi dan minta konfirmasi sebelum perubahan destruktif.



Jika Calamares tidak kompatibel dengan pendekatan build, cari alternatif installer Linux yang matang. Jangan membuat installer partisi sendiri dari nol kecuali benar-benar diperlukan.



9\. BRANDING



Buat identitas FastOS:



\- Logo original.

\- Wallpaper bawaan.

\- Tema GTK.

\- Tema ikon.

\- Tema kursor.

\- Tampilan login.

\- Boot splash jika kompatibel.

\- About FastOS.

\- Informasi versi.

\- Informasi base distribution dan kernel.



Gunakan nama produk FastOS untuk desktop, aplikasi bawaan, dan dokumentasi. Jangan menyembunyikan identitas Debian yang menjadi basis sistem.



Simpan aset buatan sendiri di direktori proyek yang terorganisasi.



10\. STRUKTUR REPOSITORY



Mulai dengan struktur yang mudah dipahami dan dirawat:



FastOS/

├── README.md

├── LICENSE

├── docs/

│   ├── ARCHITECTURE.md

│   ├── BUILD.md

│   ├── VIRTUALBOX.md

│   ├── PERFORMANCE.md

│   └── TROUBLESHOOTING.md

├── config/

│   ├── packages.list

│   ├── services/

│   ├── desktop/

│   ├── branding/

│   └── installer/

├── fastware/

│   ├── app.py

│   ├── ui/

│   ├── services/

│   ├── catalog/

│   ├── package\_manager/

│   └── tests/

├── scripts/

│   ├── bootstrap.sh

│   ├── build-iso.sh

│   ├── test-build.sh

│   ├── benchmark.sh

│   └── verify-iso.sh

├── tests/

├── assets/

│   ├── wallpapers/

│   ├── icons/

│   └── themes/

├── packaging/

└── build/



Kamu boleh menyesuaikan struktur ini, tetapi jangan membuat file kosong sekadar memenuhi struktur. Setiap komponen yang dibuat harus punya tujuan.



Direktori output build harus diatur agar hasil ISO tidak masuk ke Git.



11\. BUILD ISO



Ini adalah salah satu target terpenting.



Buat sistem build yang menghasilkan file ISO FastOS sungguhan dan bisa di-boot.



Persyaratan:



\- Menggunakan base Debian Stable.

\- Memasang paket yang telah ditentukan.

\- Mengonfigurasi desktop dan branding.

\- Mengintegrasikan FastWare.

\- Mengintegrasikan installer.

\- Menyediakan boot live jika metode build mendukungnya.

\- Memastikan ISO memiliki struktur boot yang benar.

\- Memastikan dependensi paket konsisten.

\- Menghasilkan checksum SHA-256.

\- Menyimpan log build.

\- Menghasilkan laporan error yang jelas.

\- Menjelaskan kebutuhan RAM, ruang disk, jaringan, dan hak akses untuk membangun ISO.



Jangan mengunduh ISO dari proyek lain lalu mengganti namanya menjadi FastOS.



Jangan mengklaim ISO sudah berhasil dibuat apabila build belum benar-benar selesai.



Jika environment Claude Code saat ini tidak mendukung build ISO, tetap selesaikan konfigurasi proyek dan skrip build. Jelaskan perintah yang harus dijalankan pada mesin Linux yang sesuai.



Utamakan build dari Linux host. Jika pengguna saat ini menggunakan Windows atau Termux, jelaskan keterbatasan dan rekomendasikan build di Debian/Ubuntu VM atau host Linux yang memadai.



Hindari menjalankan proses build besar secara otomatis sebelum memeriksa kapasitas disk, RAM, dependensi, dan environment.



12\. PENGUJIAN WAJIB



Buat automated tests untuk:



\- Katalog aplikasi FastWare.

\- Validasi ID paket.

\- Deteksi aplikasi terpasang.

\- Penanganan kegagalan instalasi.

\- Penanganan kegagalan jaringan.

\- Validasi operasi uninstall.

\- Struktur file konfigurasi.

\- Keamanan pemanggilan package manager.

\- Integrasi desktop entry.



Tambahkan pemeriksaan konfigurasi build dan dependensi.



Setelah ISO dibuat, siapkan pengujian di VirtualBox:



1\. Boot ISO.

2\. Periksa desktop dan resolusi.

3\. Uji mouse dan keyboard.

4\. Periksa jaringan.

5\. Buka FastWare.

6\. Cari aplikasi.

7\. Instal aplikasi kecil dari sumber yang dikonfigurasi.

8\. Buka aplikasi yang terpasang.

9\. Uji pengaturan tema.

10\. Instal FastOS ke disk virtual.

11\. Reboot dari disk virtual.

12\. Login ke akun yang dibuat.

13\. Periksa kestabilan sistem.

14\. Jalankan benchmark idle.

15\. Periksa log error.



Pisahkan hasil pengujian menjadi:



\- LULUS.

\- GAGAL.

\- BELUM DIUJI.



Jangan mengklaim pengujian VirtualBox berhasil jika kamu tidak benar-benar menjalankannya.



13\. KUALITAS DAN KEAMANAN



\- Jangan menghapus data pengguna.

\- Jangan menjalankan operasi disk destruktif tanpa konfirmasi.

\- Jangan memasukkan password, token, atau API key ke repository.

\- Jangan mengunduh skrip root dari sumber yang tidak tepercaya.

\- Jangan menonaktifkan mekanisme keamanan hanya untuk mengejar performa.

\- Jangan menambahkan telemetry tanpa persetujuan yang jelas.

\- Jangan membuat service latar belakang yang tidak diperlukan.

\- Jangan mengabaikan lisensi software.

\- Jangan menggunakan nama atau aset proprietary tanpa izin.

\- Gunakan penanganan error yang benar.

\- Gunakan konfigurasi yang bisa direproduksi.

\- Hindari hardcoding path yang spesifik pada satu mesin.



Buat file .gitignore yang sesuai, termasuk hasil build, ISO, cache, file sementara, dan rahasia.



14\. CARA KERJA CLAUDE CODE



Kerjakan proyek dalam fase yang terukur.



Fase 1 — Environment audit



Periksa:



\- Sistem operasi host.

\- Arsitektur CPU.

\- Ketersediaan Python, Git, dan utilitas build.

\- Kapasitas RAM dan disk.

\- Ketersediaan KVM atau virtualisasi jika relevan.

\- Apakah environment dapat membangun ISO Linux.

\- Apakah paket yang dibutuhkan tersedia.



Jangan langsung menjalankan sudo, mengubah sistem host, atau memasang paket global tanpa memeriksa environment dan meminta izin ketika diperlukan.



Fase 2 — Foundation



\- Buat struktur repository.

\- Buat dokumentasi arsitektur.

\- Buat konfigurasi paket.

\- Buat konfigurasi desktop.

\- Buat skrip build awal.



Fase 3 — Desktop dan branding



\- Konfigurasi XFCE.

\- Konfigurasi panel dan dock.

\- Buat tema dan wallpaper.

\- Tambahkan menu aplikasi.

\- Uji konfigurasi melalui sesi desktop jika tersedia.



Fase 4 — FastWare



\- Implementasikan aplikasi native.

\- Buat katalog aplikasi.

\- Implementasikan instalasi, status, dan uninstall dengan aman.

\- Buat automated tests.



Fase 5 — Installer dan ISO



\- Integrasikan installer.

\- Konfigurasi live boot.

\- Bangun ISO.

\- Verifikasi checksum dan struktur boot.

\- Perbaiki kegagalan build.



Fase 6 — VirtualBox dan optimasi



\- Uji ISO di VirtualBox jika environment memungkinkan.

\- Uji instalasi ke disk virtual.

\- Ukur resource.

\- Optimalkan service yang terbukti tidak diperlukan.

\- Jalankan ulang benchmark.



Fase 7 — Release



\- Lengkapi dokumentasi.

\- Catat versi dan tanggal build.

\- Buat checksum SHA-256.

\- Buat laporan pengujian.

\- Berikan instruksi menjalankan FastOS di VirtualBox.



Jangan berhenti setelah fase pertama. Setelah setiap fase, evaluasi hasil dan lanjutkan ke fase berikutnya selama tidak ada blocker nyata.



Jika ada kendala, jelaskan penyebabnya, lakukan diagnosis, dan implementasikan solusi yang aman. Jangan mengganti proyek menjadi website, mockup, atau simulasi.



Jika sebuah fitur terlalu besar, buat versi minimum yang benar-benar berfungsi terlebih dahulu.



15\. DEFINITION OF DONE



FastOS versi awal dianggap selesai ketika:



\- Repository berisi implementasi nyata.

\- Skrip build terdokumentasi dan dapat dijalankan.

\- ISO sungguhan berhasil dibangun.

\- ISO dapat di-boot di VirtualBox.

\- Desktop FastOS berfungsi.

\- Pengguna dapat menginstal FastOS ke disk virtual.

\- Sistem dapat boot dari hasil instalasi.

\- FastWare dapat dibuka sebagai aplikasi desktop native.

\- FastWare dapat mencari dan memasang aplikasi yang didukung.

\- Aplikasi terpasang dapat dijalankan.

\- Tidak ada tombol utama yang sekadar dekoratif.

\- Penggunaan RAM dan CPU telah diukur.

\- Hasil pengujian dan keterbatasan dilaporkan secara jujur.

\- Dokumentasi menjelaskan cara build dan menjalankan ISO.



Mulai sekarang dengan Fase 1. Audit environment yang benar-benar tersedia, lalu implementasikan FastOS secara bertahap. Jangan hanya menjawab dengan rencana: buat file proyek, implementasikan komponen inti, jalankan pengujian yang tersedia, dan teruskan sampai mencapai hasil yang bisa dibuktikan.

