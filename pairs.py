import re

pairs = {
# RULES FOR KTP
    'ktp' : [
        ['(surat terang panjang kartu tanda penduduk|buat surat panjang kartu tanda penduduk)', [
            'Semua KTP sifatnya sudah elektrik yang mana artinya KTP tersebut sudah bisa digunakan seumur hidup. Meskipun tertera tanggal berlaku pada KTP maka diabaikan saja (karena KTP cetakan pertama masih tertera tanggal berlakunya).',
            'tidak ada surat perpanjangan KTP',
        ]],
        ['(surat terang buat kartu tanda penduduk)', [
            'tidak ada surat keterangan pembuatan KTP',
            'tidak ada surat keterangan pembuatan KTP, untuk membuat KTP hanya diperlukan Fotocopi Kartu Keluarga dan langsung ke Kantor Catatan Sipil Setempat.',
            'Tidak diperlukan surat keterangan dalam proses pembuatan KTP. Anda hanya perlu membawa fotokopi Kartu Keluarga (KK) dan mendatangi Kantor Catatan Sipil setempat.'
        ]],
        ['(terang pindah kartu tanda penduduk)', [ 'Apabila alamat KTP Anda berada di luar Desa Melati II dan Anda sudah menetap di Desa Melati II, Anda diwajibkan membuat surat pindah dari daerah asal. Hal ini bertujuan agar administrasi Anda sesuai dengan tempat tinggal Anda saat ini. Prosesnya melibatkan membawa Kartu Keluarga asli ke Kantor Desa setempat beserta data alamat tujuan pindah.', ]] ,
        ['(terang datang kartu tanda penduduk)', [ 'E-KTP sifatnya sudah seumur hidup, maka tidak bisa diganti apabila tidak ada elemen yang harus digantikan.', ]],
        ['(terang lahir kartu tanda penduduk)', [ 'Warga Negara Indonesia (WNI) yang diwajibkan memiliki KTP Elektronik (e-KTP) adalah mereka yang telah berusia 17 tahun. Oleh karena itu, apabila anak Anda telah berusia 17 tahun, ia sudah dapat melakukan perekaman KTP di Kantor Catatan Sipil setempat.', ]],
        ['(surat terang mati kartu tanda penduduk|surat terang mati ubah status kartu|surat keterangan kematian)', [
            'Mengubah status perkawinan pada Kartu Tanda Penduduk (KTP) setelah pasangan meninggal adalah prosedur yang perlu dilakukan untuk menyesuaikan data kependudukan dengan kondisi yang sebenarnya. Adapun dokumen yang perlu dibawa yaitu KTP asli dan fotokopi, Kartu Keluarga asli dan fotokopi, Akta Kematian, Surat keterangan kematian, dan pas foto terbaru.', 
        ]],
        ['(buat ubah data kartu tanda penduduk|buat ubah data kartu keluarga)', [ 'Jika alamat Kartu Keluarga sudah sesuai dengan domisili saat ini, maka Anda hanya perlu membawa fotokopi KK dan KTP asli ke Kantor Catatan Sipil untuk perubahan KTP.', ]],
        ['(surat tempat tinggal kartu tanda penduduk)', [ 'Tidak diperlukan pembuatan Surat Keterangan Domisili jika alamat pada Kartu Keluarga (KK) telah sesuai dengan tempat tinggal saat ini. Pemohon cukup membawa fotokopi Kartu Keluarga dan Kartu Tanda Penduduk (KTP) asli ke Kantor Catatan Sipil untuk melakukan perubahan data pada KTP.', ]],
        ['(riwayat tanah kartu tanda penduduk|sk tanah status kartu tanda penduduk)', [
            'Tidak perlu membuat surat keterangan riwayat tanah jika anda ingin mengubah data pada KTP anda', 
        ]],
        ['(salin ubah kartu tanda penduduk)', [ 'Masyarakat tidak perlu membuat surat salinan C untuk membuat atau mengubah status pada KTP mereka', ]],
        ['(cara buat salin c kantor desa|cara buat surat salin kantor desa|salin c ubah status kartu tanda penduduk)', [
            'Masyarakat tidak perlu membuat surat salinan C untuk membuat atau mengubah status pada KTP mereka',
        ]],
        ['(perlu buat kartu tanda penduduk elektronik|perlu kartu tanda penduduk elektronik buat)', [
            'Saat ini semua KTP sudah wajib e-KTP dan sudah dapat digunakan untuk semua keperluan administrasi yang dibutuhkan.', 
        ]],
        ['(cara buat kartu tanda penduduk|cara buat kartu tanda penduduk elektronik|kartu tanda penduduk elektronik kantor desa)', [
            'Cara membuat KTP adalah, masyarakat hanya perlu memfotokopi Kartu Keluarga dan pergi ke Kantor Catatan Sipil Setempat.', 
        ]],
        ['(cara baik kartu tanda penduduk salah|cara baik data kartu tanda penduduk|dokumen lengkap baik kartu tanda penduduk)', [
            'Cara memperbaiki data KTP yang sudah terlanjur salah adalah dengan membawa KTP asli dan elemen pendukung data yang sebenarnya Kartu Keluarga dan Akta Kelahiran',
        ]],
        ['(buat kartu tanda penduduk perlu lurah|surat antar buat kartu tanda penduduk|terang pindah ubah alamat kartu tanda penduduk)', [
            'Tidak diperlukan surat keterangan dalam proses pembuatan KTP. Anda hanya perlu membawa fotokopi Kartu Keluarga (KK) dan mendatangi Kantor Catatan Sipil setempat.'
        ]],
        ['(dokumen data banding|dokumen buat kartu tanda duduk|perlu bawa dokumen)', [
            'Ya. Anda perlu membawa dokumen lain seperti ijazah, Akta Kelahiran, dan Kartu Keluarga sebagai data pembanding.',
            'Anda perlu membawa dokumen lain seperti ijazah, Akta Kelahiran, dan Kartu Keluarga sebagai data pembanding.',
        ]],
        ['(salin kartu tanda duduk|simpan kartu tanda duduk|mesin dapat salin)', [
            'Tidak ada informasi terkait hal tersebut',
        ]],
    ],

# RULES FOR SURAT PINDAH
    'surat_pindah' : [
        ['(kartu tanda penduduk|ubah alamat kartu tanda penduduk)', [
            'Apabila alamat KTP Anda berada di luar Desa Melati II dan Anda sudah menetap di Desa Melati II, Anda diwajibkan membuat surat pindah dari daerah asal. Hal ini bertujuan agar administrasi Anda sesuai dengan tempat tinggal Anda saat ini. Prosesnya melibatkan membawa Kartu Keluarga asli ke Kantor Desa setempat beserta data alamat tujuan pindah.',
            'Tidak diperlukan surat keterangan dalam proses pembuatan KTP. Anda hanya perlu membawa fotokopi Kartu Keluarga (KK) dan mendatangi Kantor Catatan Sipil setempat.'
        ]] ,

        ['(surat pindah)', [ 'Surat Pindah merupakan dokumen yang telah di keluarkan dari Desa ataupun Dukcapil (apabila pindah sudah beda kabupaten) yang menerangkan bahwa telah pindah dari Desa Asal ke Desa Tujuan.' ]] ,
        ['(buat surat pindah)', [ 'Cara membuat Surat Keterangan Pindah dengan membawa Kartu Keluarga asli ke Kantor Desa setempat dan data alamat tujuan pindah.' ]] ,
        ['(siapa aju surat pindah)', [ 'Masyarakat yang dapat membuat surat keterangan pindah datang adalah penduduk yang berpindah domisili dari satu tempat ke tempat lain. Surat ini diterbitkan oleh Disdukcapil atau unit pelaksana di daerah tujuan dan berfungsi sebagai bukti pindah domisili.', ]] ,
        ['(syarat buat surat pindah)', [
            'Anda harus membawa dokumen pelengkap ke Kantor Desa. Adapun dokumen pelengkap yang dibutuhkan adalah Kartu Keluarga Asli dan Alamat Tujuan pindah.',
        ]] ,
        ['(syarat aju surat pindah|cara aju surat pindah)', [
            'Persyaratan untuk membuat surat keterangan pindah datang biasanya meliputi surat pengantar dari RT/RW, fotokopi KTP dan KK, formulir permohonan pindah, dan persyaratan lain yang mungkin diperlukan oleh Disdukcapil setempat.',
            'Anda dapat mendatangi Kantor Desa tujuan pindah dengan membawa dokumen pendukung lainnya.',
        ]] ,
        ['(proses buat surat pindah|lama buat surat pindah)', [
            'Apabila hanya pindah antar Desa perkiraan waktu kurang lebih 10 menit.' 
        ]] ,
        ['(lanjut kena surat pindah|lebih lanjut surat pindah|informasi lebih surat pindah)', [
            'Untuk mendapatkan informasi lebih mengenai pembuatan surat pindah dan hal hal yang berhubungan, anda dapat bertanya melalui Kepala Dusun atau Kepala Desa',
            'Informasi mengenai kepengurusan surat pindah dapat didapat melalui Kepala Dusun dan di Kantor Desa',
        ]] ,
        ['(biaya buat surat pindah)', [ 'Tidak ada biaya yang harus dikeluarkan' ]] ,
        ['(aju surat pindah online)', [
            'Untuk saat ini masyarakat belum bisa mengajukan pembuatan Surat Pindah secara Online.',
            'Saat ini sistem yang tersedia masih belum dapat mendukung untuk pembuatan surat secara online',
        ]] ,
        ['(laku dapat surat)', [ 'Setelah mendapatkan surat pindah makan Anda dapat menyerahkan surat pindah tersebut ke kantor Desa yang menjadi tujuan untuk nantinya dibuatkan formulir untuk pembuatan Kartu Keluarga.' ]] ,
        ['(buat surat pindah)', [
            'Seseorang yang memenuhi syarat dengan menunjukkan dokumen yang diperlukan.',
            'Anda dapat mendatangi Kantor Desa tujuan pindah dengan membawa dokumen pendukung lainnya.',
        ]] ,
        ['(surat pindah terus)', [ 'Anda dapat menyerahkan surat pindah tersebut ke kaantor Desa yang menjadi tujuan jika anda sedang mengurus suatu dokumen yang harus menyertakan surat keterangn pindah. Namun jika tidak ada dokumen yang sedang anda urus, maka anda dapat menyimpannya.' ]] ,
    ],

# RULES FOR SURAT KETERANGAN DATANG
    'keterangan_datang' : [
        ['(ubah status kartu tanda duduk)', [
            'E-KTP sifatnya sudah seumur hidup, maka tidak bisa diganti apabila tidak ada elemen yang harus digantikan.',
        ]],
        ['(surat terang datang)', [ 'Surat Keterangan Datang (SKDWNI) adalah surat yang diterbitkan oleh Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) untuk membuktikan bahwa seseorang telah pindah dan menetap di daerah baru. SKDWNI digunakan sebagai dasar untuk melakukan perubahan atau penerbitan Kartu Keluarga (KK) dan KTP-el baru bagi penduduk yang bersangkutan.', ]],
        ['(buat surat terang datang)', ['Untuk pembuatan Surat Keterangan Datang, Anda perlu membawa Kartu Keluarga (KK) asli yang bersangkutan dan Kartu Keluarga dari rumah yang Anda kunjungi. Surat Keterangan Datang ini setara dengan Surat Keterangan Berkunjung.']],
        ['(bikin surat terang datang)', ['Membawa Kartu Keluarga yang berksangkutan dan Kartu Keluarga rumah yang dikunjungi. Surat Keterangan Datang sama dengan Surat Keterangan Berkunjung.']],
    ],

# RULES FOR SURAT TANAH
    'surat_tanah' : [
        ['(a)', [ 'Fotokopi KTP dari dua orang saksi (yang masih dalam satu kabupaten).', ]],
        ['(kartu tanda penduduk)', [ 
            'Tidak perlu membuat surat keterangan riwayat tanah jika anda ingin mengubah data pada KTP anda', 
            'Tidak diperlukan surat keterangan dalam proses pembuatan KTP. Anda hanya perlu membawa fotokopi Kartu Keluarga (KK) dan mendatangi Kantor Catatan Sipil setempat.'
        ]],
    ],

# RULES FOR SURAT KETERANGAN LAHIR
    'keterangan_lahir' : [
        ['(buat surat terang lahir)', [
            'surat keterangan lahir tidak dikeluarkan oleh kantor desa, melainkan oleh kantor catatan sipil dalam bentuk akta kelahiran. persyaratan pembuatan akta kelahiran adalah sebagai berikut:fotokopi kartu keluarga, fotokopi buku nikah orang tua, fotokopi ktp orang tua, fotokopi ktp dari dua orang saksi (yang masih dalam satu kabupaten), surat keterangan lahir dari bidan atau rumah sakit (asli), yang dibawa ke kantor desa setempat untuk dilengkapi dengan formulir pembuatan akta kelahiran',
        ]],
        ['(surat terang lahir kartu tanda penduduk|ubah status kartu tanda penduduk)', [
            'Warga Negara Indonesia (WNI) yang diwajibkan memiliki KTP Elektronik (e-KTP) adalah mereka yang telah berusia 17 tahun. Oleh karena itu, apabila anak Anda telah berusia 17 tahun, ia sudah dapat melakukan perekaman KTP di Kantor Catatan Sipil setempat.',
        ]],
        
        ['(surat terang lahir)', ['Surat Keterangan lahir biasanya dikeluarkan oleh Puskesmas/Tempat Bersalin/Rumah sakit tempat si bayi lahir.']]
    ],

# RULES FOR KARTU KELUARGA
    'kk': [
        ['(ganti kartu keluarga|syarat ubah kartu keluarga|buat baru ubah kartu keluarga)', [
            'Anda hanya perlu membawa Kartu Keluarga Asli, data dasar perubahan, dan mengisi formulir perubahan.',
        ]],
        ['(ubah kartu keluarga|cara ubah kartu keluarga|ubah kartu keluarga kantor)', [
            'cara membuat perubahan data pada Kartu Keluarga dengan membawa Kartu Keluarga Asli dan elemen Pendukung Perubahan tersebut (seperti Ijazah atau Akta Kelahiran) serta membawa Materai 10.000.'
        ]],
        ['(cara buat kartu keluarga)', ['cara membuat kartu keluarga yaitu apabila keluarga tersebut baru menikah maka keluarga tersebut melakukan pemecahan KK dari kedua orang tuanya masing-masing.']],
        ['(lama proses buat|lama buat kartu keluarga|waktu buat kartu keluarga)', [
            'Dalam pembuatan Kartu keluarga, pelayanan dari kantor Desa hanya sebatas sampai dengan pengisian formulir, untuk proses selanjutnya berada di Kantor Dinas Catatan Sipil.',
            'Pelayanan dari kantor Desa hanya sebatas sampai dengan pengisian formulir, untuk proses selanjutnya berada di Kantor Dinas Catatan Sipil.'
        ]],
        ['(kartu keluarga hilang|kartu keluarga rusak)', [
            'Jika Kartu Keluarga hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.',
            'ketika Kartu Keluarga anda hilang, anda dapat membuat laporan ke Polsek dengan dasar surat dari Desa.',
        ]],
        ['(keluarga kartu keluarga)', ['Kartu Keluarga adalah kartu identitas keluarga yang memuat data tentang susunan, hubungan dan jumlah anggota keluarga.']],
        ['(kartu keluarga online)', [ 
            'Untuk saat ini masyarakat belum bisa mengajukan pembuatan Kartu Keluarga secara Online.',
            'Saat ini sistem belum mendukung untuk pembuatan kartu Keluarga secara online. Ada bisa membuat Kartu Keluarga melalui Dinas Catatan Sipil'
        ]],
        ['(cara dapat kartu keluarga)', ['Seseorang akan mendapatkan Kartu Keluarga apabila keluarga tersebut baru menikah maka keluarga tersebut melakukan pemecahan KK dari kedua orang tuanya masing-masing.']],
        ['(hak dapat kartu keluarga|siapa dapat kartu keluarga)', ['Setiap keluarga wajib memiliki Kartu Keluarga']],
        ['(syarat kartu keluarga baru)', ['Syarat untuk membuat Kartu Keluarga baru adalah dengan membawa Kartu Keluarga Dasar asli (Kartu Keluarga pada keluarga sebelumnya) dan Buku Menikah.']],
        ['(biaya buat kartu keluarga)', ['Tidak ada biaya yang harus dikeluarkan']],

        ['(ubah data kartu tanda duduk)', [
            'Ya. Apabila jika data di Kartu Keluarga dan KTP terdapat elemen yang salah, maka harus melakukan Perubahan dahulu.',
            'Jika alamat Kartu Keluarga sudah sesuai dengan domisili saat ini, maka Anda hanya perlu membawa fotokopi KK dan KTP asli ke Kantor Catatan Sipil untuk perubahan KTP.',
        ]],
        ['(buat kartu tanda duduk)', [
            'Tidak diperlukan surat keterangan dalam proses pembuatan KTP. Anda hanya perlu membawa fotokopi Kartu Keluarga (KK) dan mendatangi Kantor Catatan Sipil setempat.',
        ]],
        ['(surat antar lurah)', [
            'Ya, ada beberapa dokumen yang dibutuhkan untuk membuat KTP. Tetapi tidak Ada surat Pengantar, hanya Fotokopi Kartu Keluarga saja.',
        ]],
        ['(dokumen ijazah kartu keluarga)', [
            'Cara memperbaiki data KTP yang sudah terlanjur salah adalah dengan membawa KTP asli dan elemen pendukung data yang sebenarnya Kartu Keluarga dan Akta Kelahiran',
        ]],
    ],

# RULES FOR SURAT DOMISILI TEMPAT TINGGAL
    'domisili' : [
        ['(tinggal ubah alamat kartu tanda penduduk)', [
            'Tidak diperlukan pembuatan Surat Keterangan Domisili jika alamat pada Kartu Keluarga (KK) telah sesuai dengan tempat tinggal saat ini. Pemohon cukup membawa fotokopi Kartu Keluarga dan Kartu Tanda Penduduk (KTP) asli ke Kantor Catatan Sipil untuk melakukan perubahan data pada KTP.'
            'Tidak. Apabila Kartu Keluarga sudah beralamat/berdomisili ditempat tersebut, maka hanya perlu membawa fotocopi KK dan KTP asli ke Kantor Catatan Sipil untuk perubahan KTP.',
        ]] ,

        ['(surat domisili tempat tinggal)', ['Surat Domisili tempat tinggal merupakan surat yang menerangkan tempat tinggal dari warga tersebut.']] ,
        ['(cara buat surat domisili tempat tinggal|cara buat surat terang pindah)', [
            'Cara membuat surat domisili tempat tinggal di Kantor Desa dengan harus membuat Surat Mandah dari Desa Asal kemudian di bawa ke Kantor Desa Melati II serta membawa fotocopi KK.',
            'Apabila orang tersebut beralamat di Luar Desa Melati II, maka harus membuat Surat Mandah dari Desa Asal kemudian di bawa ke Kantor Desa Melati II serta membawa fotocopi KK.',
        ]] ,
        ['(siapa dapat surat domisili tempat tinggal)', ['setiap warga dapat memiliki surat tersebut di dukung dengan dasar-dasar yang real.']] ,
        ['(cara dapat surat domisili tempat tinggal)', ['Anda bisa langsung datang ke Kantor Desa untuk mendapatkan surat Domisili Tempat Tinggal']] ,
        ['(syarat dapat surat domisili tempat tinggal)', ['Untuk mendapatkan Surat Domisili tempat tinggal hanya perlu membawa Kartu Keluarga dan Surat Mandah saja.']] ,
        ['(proses buat surat domisili tempat tinggal)', ['Waktu yang dibutuhkan untuk membuat Surat Domisili Tempat Tinggal adalah sekitar 10 menit.']] ,
        ['(biaya buat surat domisili tempat tinggal)', ['Tidak ada biaya yang harus dikeluarkan']] ,
        ['(surat domisili tempat tinggal online)', ['Saat ini sistem belum mendukung untuk pembuatan Surat Keterangan Domisili secara online.']] ,
        ['(domisili tempat tinggal hilang rusak)', ['Jika surat domisili hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.']] ,
    ],

# RULES FOR SURAT KETERANGAN RIWAYAT TANAH
    'skrt' : [
        ['(surat|terang|riwayat|tanah|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(siapa|yang|bisa|dapat|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(syarat|untuk|dapat|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(dapat|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(berapa|lama|proses|buat|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(berapa|biaya|buat|skrt)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(bisa|dapat|skrt|online)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(yang|harus|laku|jika|skrt|hilang|atau|rusak)', ['Tidak ada informasi terkait hal tersebut']]
    ],

# RULES FOR SKCK
    'skck' : [
        ['(surat antar skck)', ['Surat Pengantar SKCK adalah surat pengantar permohonan dari Desa kepada Polsek untuk memberikan Surat Keterangan Catatan Kriminal Seseorang']] ,
        ['(cara buat surat antar)', ['Anda bisa langsung datang ke Kantor Desa untuk mendapatkan surat pengantar pembuatakan SKCK']] ,
        ['(siapa buat surat antar|buat surat antar skck)', [
            'Setiap Orang yang sudah memiliki KTP/Wajib KTP (Umur 17 Tahun) dapat membuat surat pengantar SKCK',
            'Setiap Orang yang sudah memiliki KTP/Wajib KTP (Umur 17 Tahun)',
        ]] ,
        ['(isi surat antar skck|isi surat antar surat terang catat)', ['Isi dari Surat Pengantar SKCK yaitu, menjelaskan identitas seseorang, data kedua orang tua, bukan anggota G30SPKI dan anggota organisasi terlarang lainnya.']] ,
        ['(format baku surat antar|format surat antar surat terang)', ['Ada format baku untuk surat pengantar SKCK (untuk lebih jelasnya bisa disesuaikan dengan melihat pada internet)']] ,
        ['(guna surat antar skck)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(surat antar hilang rusak)', [
            'Jika SKCK hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.'
        ]] ,
        ['(surat antar surat terang catat)', ['Surat Pengantar SKCK adalah surat pengantar permohonan dari Desa kepada Polsek untuk memberikan Surat Keterangan Catatan Kriminal Seseorang']] ,
        ['(cara buat surat antar surat terang)', [
            'Anda harus membawa dokumen pelengkap ke Kantor Desa. Adapun dokumen pelengkap yang dibutuhkan adalah Kartu Keluarga Asli dan Alamat Tujuan pindah.'
        ]] ,
        ['(mana dapat contoh surat antar surat)', ['Anda bisa mendatangi Kantor Desa']] ,
        ['(mana dapat contoh surat antar skck)', ['untuk contoh Surat Keterngan Cacatan Sipil Anda bisa mendatangi Kantor Desa']] ,
        ['(surat terang catat polisi hilang|surat terang catat polisi rusak)', [
            'Jika Surat Keterangan Catatan Sipil hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.'
        ]] ,
    ],

# RULES FOR SKTM
    'skk' : [
        ['(a)', ['Cara membuat surat Keterangan Kematian dengan membawa Kartu Keluarga Asli ke Kantor Desa setempat serta memberitahukan waktu meninggalnya (seperti Umur, Hari, Tanggal meninggalnya)']] ,
        ['(kartu tanda penduduk)', ['Mengubah status perkawinan pada Kartu Tanda Penduduk (KTP) setelah pasangan meninggal adalah prosedur yang perlu dilakukan untuk menyesuaikan data kependudukan dengan kondisi yang sebenarnya. Adapun dokumen yang perlu dibawa yaitu KTP asli dan fotokopi, Kartu Keluarga asli dan fotokopi, Akta Kematian, Surat keterangan kematian, dan pas foto terbaru.']] ,
    ],

# RULES FOR UMUM
    'umum' : [
        ['(buka)', [
            'Selamat datang di Chatbot Desa Melati 2. Anda bisa menanyakan terkait informasi yang ingin diketahui melalui layanan ini. Pertanyaan yang bisa diajukan berkaitan dengan 1. PROFIL Desa Melati 2, 2. Tatacara kepengurusan surat yang sifatnya administratif.',
        ]] ,
        ['(sifat)', ['Surat yang bersifat administratif adalah jenis surat yang berisi informasi tentang kegiatan administrasi, seperti laporan, pemberitahuan, permintaan, dan pernyataan. Surat ini digunakan untuk memberikan pesan atau informasi secara tertulis dari satu pihak ke pihak lain dalam organisasi atau instansi pemerintahan.']] ,
        ['(jenis)', [
"""Pelayanan Administrasi Kependudukan:
1. Surat Keterangan Pembuatan KTP
3. Surat Keterangan PINDAH
4. Surat Keterangan DATANG
5. Surat Keterangan Lahir
6. Surat Keterangan Kematian
7. Perubahan Data KK
8. Surat Keterangan Riwayat Tanah
Pelayanan Ketentraman dan Ketertiban (TRANTIB): 
1. Surat Pengantar SKCK
2. Surat Pengantar Ijin Rame-rame(Izin Keramaian)""",
        ]] ,
    ],

    # RULES FOR SKTM
    'sktm' : [
        ['(surat terang mampu sktm)', ['Surat Keterangan Tidak Mampu (SKTM) adalah surat yang menyatakan kondisi ekonomi suatu keluarga dianggap lemah atau tidak mampu']] ,
        ['(hak dapat sktm)', ['Seseorang yang dapat menerima SKTM adalah mereka yang masuk kedalam kategori warga tidak mampu dalam perekonomian']] ,
        ['(syarat dapat sktm)', ['Syarat membuat Surat Keterangan Tidak mampu adalah dengan membawa Kartu Keluarga asli dan fotokopi nya ke Kantor Desa setempat.']] ,
        ['(cara dapat sktm|cara punya surat terang mampu)', [
            'Anda bisa langsung datang ke Kantor Desa untuk mendapatkan surat pengantar pembuatakan SKTM'
        ]] ,
        ['(proses buat sktm|proses buat surat terang)', ['Waktu yang dibutuhkan untuk membuat SKTM adalah sekitar 10 menit.']] ,
        ['(biaya buat sktm|biaya buat surat terang)', ['Tidak ada biaya yang harus dikeluarkan']] ,
        ['(dapat sktm online|surat terang mampu online)', ['Saat ini sistem belum mendukung untuk pembuatan Surat Keterangan Tidak Mampu secara online.']] ,
        ['(milik surat terang|punya surat terang mampu|dapat surat terang)', [
            'Seseorang yang dapat menerima SKTM adalah mereka yang masuk kedalam kategori warga tidak mampu dalam perekonomian'
        ]] ,
        ['(syarat dapat surat terang)', ['Syarat membuat Surat Keterangan Tidak mampu adalah dengan membawa Kartu Keluarga asli dan fotokopi nya ke Kantor Desa setempat.']] ,
        ['(sktm hilang rusak|surat terang mampu hilang|surat terang mampu rusak)', [
            'Jika SKTM hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.',
            'Jika Surat Keterangan Tidak Mampu hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.',
        ]] ,
    ],

# RULES FOR  SKU
    'sku' : [
        ['(surat terang usaha sku)', ['Surat Keterangan usaha adalah surat yang menerangkan tentang usaha seseorang']] ,
        ['(siapa dapat sku|siapa dapat surat terang usaha)', [
            'Warga yang dapat memiliki Surat Keterangan Usaha (SKU) adalah seseorang yang memiliki usaha milik sendiri.'
        ]] ,
        ['(syarat dapat sku|syarat dapat surat terang usaha)', [
            'Syarat untuk mendapatkan SKU adalah fotocopy Kartu Keluarga atau fotocopy KTP serta membawa foto usaha yang sedang dijalankan'
        ]] ,
        ['(cara dapat sku|cara dapat surat terang usaha)', [
            'Anda bisa langsung datang ke Kantor Desa untuk mendapatkan surat pengantar pembuatakan Surat Keterangan Usaha (SKU)'
        ]] ,
        ['(lama proses sku|waktu buat surat terang usaha)', [
            'Waktu yang dibutuhkan untuk membuat SKU adalah sekitar 10 menit.'
        ]] ,
        ['(biaya buat sku|biaya buat surat terang usaha)', [
            'Tidak ada biaya yang harus dikeluarkan'
        ]] ,
        ['(sku online|surat terang usaha online)', [
            'Untuk saat ini masyarakat belum bisa mengajukan pembuatan Surat Keterangan Usaha secara Online.'
        ]] ,
        ['(sku hilang rusak|surat terang usaha hilang|surat terang usaha rusak)', [
            'Jika Surat Keterangan Usaha hilang atau rusak, anda dapat membuat laporan ke Kantor Desa.'
        ]] ,
    ],

# RULES FOR KIA
    'kia' : [
        ['(terang lahir)', ['Surat Keterangan Lahir tidak dikeluarkan oleh Kantor Desa, melainkan oleh Kantor Catatan Sipil dalam bentuk Akta Kelahiran. Persyaratan pembuatan Akta Kelahiran adalah sebagai berikut:Fotokopi Kartu Keluarga, Fotokopi buku nikah orang tua, Fotokopi KTP Orang tua, Fotokopi KTP dari dua orang saksi (yang masih dalam satu kabupaten), Surat keterangan lahir dari bidan atau rumah sakit (Asli), yang dibawa ke Kantor Desa setempat untuk dilengkapi dengan formulir pembuatan Akta Kelahiran']],
        ['(informasi lebih lanjut)', ['Anda bisa mendapatkan informasi lebih mendalam mengenai KIA melalui Kepala Desa, Dinas Kependudukan dan Catatan Sipil, serta dari internet.']],
        ['(cara buat kartu)', ['Dengan membawa fotocopy Kartu Keluarga, fotocopy Akta Kelahiran dan Pasphoto 4x6(bagi yang berumur diatas 6 Tahun)']],
        ['(siapa dapat kartu)', ['Kartu Identitas Anak hanya diperuntukkan bagi anak anak dengan rentan usia 0-5 tahun dan 5-17 tahun kurang dari satu hari.']],
        ['(kia)', ['KIA merupakan Kartu identitas seorang anak yang berlaku sampai usia 16 tahun dalam arti lain ini merupakan "KTP" nya anak-anak']],
        ['(manfaat kartu|manfaat kia)', ['Manfaat dari Kartu Identitas Anak adalah sebagai kartu identitas, sama halnya dengan Kartu Tanda Penduduk (KTP)']],
        ['(biaya buat kartu)', ['Pembuatan KIA tidak dipungut biaya']],
        ['(anak usia bawah)', ['tidak diwajibkan bagi anak usia dibawah 5tahun untuk memiliki KIA tetapi disarankan memiliki KIA']],
        ['(buka rekening bank)', ['Tidak. Karena syarat pembukaan Rekening Baru harus memiliki KTP-El']],
        ['(untuk naik pesawat)', ['Untuk informasi mengenai ini mungkin dapat dicari melalui internet']]
    ],

# RULES FOR PROFIL
    'profil' : [
        ['(lokasi)', ['Desa Melati II Kecamatan Perbaungan Kabupaten Serdang Bedagai Provinsi Sumatera Utara']] ,
        ['(luas wilayah)', ['Luas Desa Melati II yaitu 1180 Ha']] ,
        ['(jumlah duduk)', ['Jumlas penduduk dari Desa Melati 2 yaitu 18.231 Jiwa']] ,
        ['(jumlah duduk lakilaki)', ['Jumlah penduduk laki laki di Desa Melati 2 yaitu 8.618']] ,
        ['(jumlah duduk perempuan)', ['Jumlah penduduk perempuan di Desa Melati 2 yaitu 9.613']] ,
        ['(kepala)', ['Pemimpin dari Desa Melati 2 yaitu seorang Kepala Desa']],
        ['(sejarah singkat)', ['Menurut sejarah Desa Melati II adalah perjuangan Bapak Siswuyuono, dimana tanah Desa yang sekarang dinamakan Desa Melati II antara tahun 1948-1960 terbentuklah nama Kampung Melati. Dimana waku itu Bapak Siswuyuono menaman Pohon Bunga Melati bersama masyarakat di sekitar perkampungan dan tumbuh hingga saat ini. Lambat laun Kampung Melati tersebut bertambah ramai dan sesuai dengan tuntutan dan perkembangan zaman, saat ini kampung Melati telah berubah menjadi Desa Melati, maka jelaslah asal nama Melati II adalah pemetaan wilayah antara Kelurahan Melati I dan Desa Melati II.']] ,
        ['(budaya)', ['Ada beberapa budaya dan suku di Desa Melati II yaitu Jawa, Banjar, Melayu, Batak, dan Nias']] ,
        ['(makanan khas)', ['Tidak ada makanan khas dari Desa Melati 2']],
        ['(tempat wisata)', ['Tempat wisata dari Desa Melati 2 yaitu Kebun Jeruk Petik Sendiri dan Palungguhan To Joyo']],
        ['(ekonomi)', ['Ekonomi di Desa Melati II tergolong ekonomi yang cukup baik']] ,
        ['(industri)', ['Industri yang ada di Desa Melati II seperti industri makanan, meubel, dan pakaian']] ,
        ['(didik)', ['Kondisi pendidikan di Desa Melati II tersedia lengkap mulai dari PAUD hingga SMA']] ,
        ['(banyak sekolah)', ['Secara total ada 42 tempat pendidikan']],
        ['(batasbatas wilayah)', ['Batasan dari wilayah Desa Melati II adalah, sebelah Utara dengan Kelurahan Melati I, Sebelah Selatan Dengan Perkebunan, Sebelah barat Dengan Desa Citaman Jernih dan Perkebunan, Sebelah Timur dengan Desa Jatimulyo']] ,
        ['(banyak rumah sakit)', ['Tidak ada Rumah Sakit di Desa Melati 2']],
        ['(agama anut duduk)', ['Ada beberapa agama para penduduk Desa Melati II, yaitu Islam, Kristen, Katolik, Hindu, dan Budha.']] ,
        ['(tingkat)', ['Dari luas 1.180 Ha, 195 Ha merupakan pemukiman masyarakat']] ,
        ['(kurang)', ['Kekuarangan dari Desa Melati II yaitu jauh dari Kawasan industri sehingga sedikit lapangan pekerjaan']] ,
        ['(unggul)', ['Keunggulan dari Desa Melati II yaitu memiliki lahan pertanian yang luas, jumlah penduduk yang banyak, jarak ke ibu kota Kecamatan dan ibu kota Kabupaten tidak Jauh.']] ,
        ['(tantang hadap)', ['Tantangan bisa menjadi Lumbung Pangan dengan potensi wilayah pertanian yang cukup luas.']],
        ['(peluang hadap)', ['Peluang bisa menjadi Lumbung Pangan dengan potensi wilayah pertanian yang cukup luas.']] ,
        ['(rencana bangun)', ['Direncanakan Desa Melati II menjadi Desa Wisata yang sejahtera dengan melibatkan warga masyarakat']] ,
        ['(suku bangsa)', ['Suku bangsa yang ada di Desa Melati II yaitu Jawa, Banjar, Melayu, Batak, Nias']],
        ['(adat istiadat)', ['Adat istiadat yang ada di Desa Melati II yaitu Jawa, Banjar, Melayu, Batak, Nias']] ,
        ['(sumber dapat)', ['APBN Daerah, Pendapatan Desa, dan Pendapatan Lain yang tidak terikat']] ,
        ['(fasilitas sehat)', ['Fasilitas kesehatan di Desa Melati II mencakup beberapa fasilitas yaitu Puskesmas, Praktek Bidan, Poliklinik, Balai Pengobatan dan Apotek']] ,
        ['(potensi ekonomi)', ['Potensi dari Desa Melati II adalah lahan pertanian, Peternakan, Wisata, jasa dan Perdagangan']],
        ['(berapa usia duduk)', ['Rata rata usia dari penduduk Desa Melati 2 yaitu 19-59 Tahun']],
        ['(sistem pemerintahan)', ['Sistem Pemerintahan Desa Murni']],
    ],
}