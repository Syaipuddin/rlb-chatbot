pairs = {

# RULES FOR KTP
    'mulai' : [
        ['(mulai|chatbot|melati)', ["SELAMAT DATANG DI CHATBOT MELATI II"
                                    " "
                                    "Anda bisa bertanya terkait informasi yang ingin anda ketahui melalui layanan ini. Adapun pertanyaan yang diajukan berkaitan dengan :"
                                     "(KTP)  (SURAT PINDAH) (SURAT KETERANGAN DOMISILI)  (SKCK)  (SKTM)  (SKU)  (KIA)  (PROFILE) "
                                    "Anda bisa mengklik salah 1 menu diatas"]],

    ],
    'profile' : [
        ['profile', ['Berikut pertanyaan mengenai PROFILE:'
                     '(Bagaimana sejarah singkat daerah tersebut?) (Apa saja budaya yang ada di Desa Melati II?) (Apa saja makanan khas daerah tersebut?) (Apa saja tempat wisata yang ada di daerah tersebut?) (Apa saja adat istiadat yang ada di daerah tersebut?)']]
    ],
    'ktp' : [
        ['(ktp)', ['Berikut pertanyaan mengenai KTP :'
                   '(Bagaimana cara buat KTP?) (Apa saja dokumen pelengkap pembuatan KTP?) (Apakah perlu membuat surat keterangan pembuatan KTP?)']],
        ['(perlu|buat|surat|terang|panjang|ktp|jika|ingin|panjang|masa|laku)', ['kalau KTP sudah elektrik, maka otomatis akan aktif seumur hidup. Meskipun tertera tanggal berlaku KTP tersebut maka dabaikan saja (karena KTP cetakan pertama masih ada tanggal berlakunya)']] ,
        ['(buat|surat|terang|panjang|ktp|kantor|desa)', ['tidak ada surat perpanjangan KTP']] ,
        ['(perlu|buat|surat|terang|buat|ktp|jika|ingin|untuk|pertama|kali)', ['tidak ada surat keterangan, untuk membuat KTP hanya diperlukan Fotocopi Kartu Keluarga dan langsung ke Kantor Catatan Sipil Setempat.']] ,
        ['(buat|surat|terang|buat|ktp|kantor|desa)', ['tidak ada surat keterangan pembuatan KTP']] ,
        ['(perlu|buat|surat|terang|pindah|jika|ingin|ubah|alamat|ktp)', ['Tentu Saja. Apabila KTP Anda beralamat di Luar Desa Melati II dan sudah menetap bertempat tinggal di Desa Melati II, maka diharuskan membuat surat Pindah dari Daerah Asal, agar administrasi Anda sesuai dengan tempat tinggal anda yang sekarang']] ,
        ['(buat|surat|terang|pindah|kantor|desa)', ['dengan membawa Kartu Keluarga Asli ke Kantor Desa Setempat dan data alamat tujuan pindah.']] ,
        ['(perlu|buat|surat|terang|datang|jika|ingin|ubah|status|ktp)', ['KTP sudah seumur hidup, maka tidak bisa diganti apabila tidak ada elemen yang harus digantikan.']] ,
        ['(buat|surat|terang|datang|kantor|desa)', ['Membawa Kartu Keluarga yang berksangkutan dan Kartu Keluarga rumah yang dikunjungi. Surat Keterangan Datang sama dengan Surat Keterangan Berkunjung.']] ,
        ['(perlu|buat|surat|terang|lahir|jika|ingin|ktp|untuk|anak)', ['WNI yang diwajibkan memiliki KTP-El adalah yang sudah berumur 17 Tahun. Maka Apabila Anak Anda sudah berumur 17 Tahun maka sudah bisa melakukan perekaman KTP di Kantor Catatan Sipil Setempat.']] ,
        ['(buat|surat|terang|lahir|kantor|desa)', ['Surat Keterangan Lahir tidak dikeluarkan dari Kantor Desa melainkan dari Kantor Catatan Sipil yakni Akta Kelahiran. Syarat pembuatan Akta Kelahiran, yaitu dengan membawa : Fotocopi Kartu Keluarga, Fotocopi Buku Nikah Orang Tua, Fotocopi KTP Orang Tua, Fotocopi KTP 2 orang saksi (yang masih dalam 1 kabupaten), Surat Keterangan Lahir dari Bidan/Rumah Sakit Asli ke Kantor Desa Setempat dan akan dilengkapi dengan Formulir pembuatan Akta Kelahiran.']] ,
        ['(perlu|buat|surat|terang|mati|jika|ingin|ubah|status|ktp)', ['Jika orang yang memiliki KTP sudah meninggal, maka KTP tersebut akan ditarik kembali oleh Kator Catatan Sipil Setempat dan akan digantikan dengan menimbulkan Akta Kematian orang tersebut.']] ,
        ['(buat|surat|terang|mati|kantor|desa)', ['dengan membawa Kartu Keluarga Asli ke Kantor Desa Setempat serta memberitahukan waktu meninggalnya (seperti Umur, Hari, Tanggal meninggalnya)']] ,
        ['(perlu|buat|ubah|data|kk|jika|ingin|ubah|ktp)', ['Ya. Apabila jika data di KK dan KTP terdapat elemen yang salah, maka harus melakukan Perubahan dahulu.']] ,
        ['(buat|ubah|data|kk|kantor|desa)', ['Dengan membawa Kartu Keluarga Asli dan elemen Pendukung Perubahan tersebut (seperti Ijazah atau Akta Kelahiran) serta membawa Materai 10.000.']] ,
        ['(perlu|buat|surat|domisili|tempat|tinggal|jika|ingin|ubah|alamat|ktp)', ['Tidak. Apabila KK sudah beralamat/berdomisili ditempat tersebut, maka hanya perlu membawa fotocopi KK dan KTP asli ke Kantor Catatan Sipil untuk perubahan KTP.']] ,
        ['(buat|surat|domisili|tempat|tinggal|kantor|desa)', ['Apabila orang tersebut beralamat di Luar Desa Melati II, maka harus membuat Surat Mandah dari Desa Asal kemudian di bawa ke Kantor Desa Melati II serta membawa fotocopi KK.']] ,
        ['(perlu|buat|surat|terang|riwayat|tanah|jika|ingin|ubah|status|ktp)', ['Tidak.']] ,
        ['(buat|surat|terang|riwayat|tanah|kantor|desa)', ['tidak pernah membuat surat keterangan riwayat tanah.']] ,
        ['(perlu|buat|surat|salin|c|jika|ingin|ubah|status|ktp)', ['tidak']] ,
        ['(buat|surat|salin|c|kantor|desa)', ['tidak pernah membuat surat salinan C.']] ,
        ['(perlu|buat|e-ktp|jika|ingin|ktp|baru)', ['Saat ini semua KTP sudah wajib e-KTP']] ,
        ['(buat|e-ktp|kantor|desa)', ['untuk membuat KTP hanya diperlukan Fotocopi Kartu Keluarga dan langsung ke Kantor Catatan Sipil Setempat.']] ,
        ['(baik|data|ktp|yang|salah)', ['membawa KTP asli dan elemen pendukung data yang sebenarnya ( KK    )']] ,
        ['(perlu|bawa|dokumen|lain|seperti|ijazah|akta|lahir|dan|kartu|keluarga|bagai|data|banding)', ['Ya.']] ,
        ['(buat|ktp|baru|kantor|desa)', ['Pembuatan KTP tidak di Kantor Desa melainkan di Kantor Catatan Sipil']] ,
        ['(perlu|bawa|surat|antar|dari|lurah|dan|foto|kopi|kartu|keluarga|ke|kantor|camat)', ['Ya. Tetapi Tidak Ada surat Pengantar. Hanya Fotocopi KK saja.']] ,
        ['(salin|e-ktp|jika|tidak|ingin|fotokopi)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(perlu|masuk|e-ktp|ke|dalam|card|reader|untuk|dapat|salin)', ['Tidak ada informasi terkait hal tersebut']]
    ],

# RULES FOR SURAT PINDAH
    'surat_pindah' : [
        ['(surat|pindah)', ['Berikut pertanyaan mengenai Surat Pindah :'
                            '(Apa yang dimaksud dengan surat pindah?) (Siapa yang bisa mengajukan surat pindah?) (Bagaimana cara mengajukan surat pindah?)']],
        ['(itu|surat|pindah)', ['Surat Pindah merupakan dokumen yang telah di keluarkan dari Desa ataupun Dukcapil (apabila pindah sudah beda kabupaten) yang menerangkan bahwa telah pindah dari Desa Asal ke Desa Tujuan.']] ,
        ['(siapa|yang|bisa|aju|surat|pindah)', ['orang yang pindah']] ,
        ['(syarat|untuk|aju|surat|pindah)', ['Kartu Keluarga Asli dan Alamat Tujuan pindah']] ,
        ['(aju|surat|pindah)', ['dengan datang ke kantor Desa membawa syarat yang ditentukan']] ,
        ['(berapa|lama|proses|buat|surat|pindah)', ['Apabila hanya pindah antar Desa perkiraan waktu kurang lebih 10 menit.']] ,
        ['(berapa|biaya|buat|surat|pindah)', ['Tidak Berbayar']] ,
        ['(bisa|aju|surat|pindah|online)', ['tidak bisa']] ,
        ['(yang|harus|laku|telah|dapat|surat|pindah)', ['serahkan surat pindah tersebut ke kaantor Desa yang menjadi tujuan. Maka akan di buatkan formulir untuk pembuatan Kartu Keluarga.']] ,
        ['(mana|bisa|dapat|informasi|lebih|lanjut|tentang|surat|pindah)', ['melalui Kepala Dusun atau Kantor Desa']]
        ],

# RULES FOR SURAT KETERANGAN DATANG
    'keterangan_datang' : [
        ['(itu|surat|terang|datang)', ['tidak ada surat keterangan datang']]
    ],

# RULES FOR SURAT KETERANGAN LAHIR
    'keterangan_lahir' : [
        ['(itu|surat|terang|lahir)', ['Surat Keterangan lahir biasanya dikeluarkan oleh Puskesmas/Tempat Bersalin/Rumah sakit tempat si bayi lahir.']]
    ],

# RULES FOR KARTU KELUARGA
    'kk': [
        ['(kartu keluarga)', ['Berikut pertanyaan mengenai Kartu Keluarga :'
                              '(Bagaimana cara mendapatkan Kartu Keluarga?) (Berapa lama proses pembuatan Kartu Keluarga?)']],
        ['(itu|kartu|keluarga|kk)', ['kartu identitas keluarga yang memuat data tentang susunan, hubungan dan jumlah anggota keluarga. ']] ,
        ['(siapa|yang|hak|dapat|kk)', ['KK wajib dimiliki oleh setiap keluarga.']] ,
        ['(dapat|kk)', ['apabila keluarga tersebut baru menikah maka keluarga tersebut melakukan pemecahan KK dari kedua orang tuanya masing-masing.']] ,
        ['(syarat|untuk|buat|kk|baru)', ['KK Dasar asli, Buku Menikah.']] ,
        ['(syarat|untuk|ubah|kk)', ['KK Asli, data dasar perubahan, mengisi formulir perubahan.']] ,
        ['(buat|kk|baru|atau|ubah|kk)', ['jawaban di pertanyaan no 60 dan 61.']] ,
        ['(berapa|lama|proses|buat|kk)', ['pelayanan dari kantor Desa hanya sebatas sampai dengan pengisian formulir, untuk proses selanjutnya berada di Kantor Dinas Catatan Sipil.']] ,
        ['(berapa|biaya|buat|kk)', ['Tidak Berbayar']] ,
        ['(bisa|buat|kk|online)', ['bisa melalui Dinas Catatan Sipil.']] ,
        ['(yang|harus|laku|jika|kk|hilang|atau|rusak)', ['membuat laporan ke Polsek dengan dasar surat dari Desa.']]
    ],

# RULES FOR SURAT DOMISILI TEMPAT TINGGAL
    'domisili' : [
        ['(surat|terang|omisili)', ['Berikut pertanyaan mengenai Surat Keterangan Domisili: '
                                         '(Apa yang dimaksud surat domisili tempat tinggal?) (Siapa saja yang bisa mendapatkan surat domisili tempat tinggal?) (Apa saja syarat untuk mendapatkan surat domisili tempat tinggal?)']],
        ['(itu|surat|domisili|tempat|tinggal)', ['Surat Domisili tempat tinggal merupakan surat yang menerangkan tempat tinggal dari warga tersebut.']] ,
        ['(siapa|yang|bisa|dapat|surat|domisili|tempat|tinggal)', ['setiap warga yang ingin mendapatkan surat tersebut di dukung dengan dasar-dasar yang real.']] ,
        ['(dapat|surat|domisili|tempat|tinggal)', ['melalui kantor Desa.']] ,
        ['(syarat|untuk|dapat|surat|domisili|tempat|tinggal)', ['Memabawa Kartu Keluarga atau Surat Mandah.']] ,
        ['(berapa|lama|proses|buat|surat|domisili|tempat|tinggal)', ['Kurang lebih 10 Menit.']] ,
        ['(berapa|biaya|buat|surat|domisili|tempat|tinggal)', ['Tidak Berbayar']] ,
        ['(bisa|dapat|surat|domisili|tempat|tinggal|online)', ['Tidak']] ,
        ['(yang|harus|laku|jika|surat|domisili|tempat|tinggal|hilang|atau|rusak)', ['Membuat Laporan Ke Kantor Desa.']]
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
        ['(skck)', ['Berikut pertanyaan mengenai SKCK: '
                    '(Apakah perlu surat pengantar untuk membuat SKCK?) (Siapa saja yang bisa membuat surat pengantar SKCK?) (Apakah ada format baku untuk surat pengantar SKCK?)']],
        ['(itu|surat|antar|skck)', ['Surat Pengantar SKCK adalah surat pengantar permohonan dari Desa kepada Polsek untuk memberikan Surat Keterangan Catatan Kriminal Seseorang']] ,
        ['(siapa|yang|bisa|buat|surat|antar|skck)', ['Setiap Orang yang sudah memiliki KTP/Wajib KTP (Umur 17 Tahun)']] ,
        ['(isi|surat|antar|skck)', ['Isi Surat Pengantar SKCK yaitu, Menjelaskan Identitas Seseorang, Data Kedua Orang Tua, Bukan anggota G30SPKI dan anggota organisasi terlarang lainnya.']] ,
        ['(buat|surat|antar|skck)', ['melalui kantor Desa.']] ,
        ['(ada|format|baku|untuk|surat|antar|skck)', ['Ada']] ,
        ['(mana|bisa|dapat|contoh|surat|antar|skck)', ['Di Kantor Desa']] ,
        ['(bisa|guna|surat|antar|skck|dari|instansi|lain)', ['Tidak ada informasi terkait hal tersebut']],
        ['(yang|harus|laku|jika|surat|antar|skck|hilang|atau|rusak)', ['Membuat yang baru ke kantor Desa']]
    ],

    # RULES FOR SKTM
    'sktm' : [
        ['(sktm)', ['berikut pertanyaan mengenai SKTM: '
                    '(Siapa saja yang bisa mendapatkan SKTM?) (Apa saja syarat untuk mendapatkan SKTM?) (Berapa biaya pembuatan SKTM?)']],
        ['(itu|surat|terang|tidak|mampu|sktm)', ['Surat yang menerangkan bahwa orang tersebut tergolong ekonomi lemah/tidak Mampu']] ,
        ['(siapa|yang|hak|dapat|sktm)', ['Warga yang dinyatakan tidak mampu dalam perekonomian ']] ,
        ['(syarat|untuk|dapat|sktm)', ['Membawa FC. KK']] ,
        ['(dapat|sktm)', ['melalui kantor Desa.']] ,
        ['(berapa|lama|proses|buat|sktm)', ['Kurang lebih 10 Menit.']] ,
        ['(berapa|biaya|buat|sktm)', ['Tidak Berbayar']] ,
        ['(bisa|dapat|sktm|online)', ['tidak']] ,
        ['(yang|harus|laku|jika|sktm|hilang|atau|rusak)', ['membuat kembali di kantor Desa']]
    ],

# RULES FOR  SKU
    'sku' : [
        ['(sku)', ['Berikut pertanyaan mengenai SKU: '
                   '(Apa pengertian Surat Keterangan Usaha?) (Bagaimana cara mendapatkan SKU?) (Apa saja syarat untuk mendapatkan Surat Keterangan Usaha?)']],
        ['(itu|surat|terang|usaha|sku)', ['Surat Keterangan usaha adalah surat yang menerangkan tentang usaha seseorang']] ,
        ['(siapa|yang|bisa|dapat|sku)', ['warga yang ingin mendapatkan surat tersebut dan benar memiliki usaha']] ,
        ['(syarat|untuk|dapat|sku)', ['FC KK atau FC KTP serta membawa Photo Usaha']] ,
        ['(dapat|sku)', ['melalui kantor Desa.']] ,
        ['(berapa|lama|proses|buat|sku)', ['Kurang lebih 10 Menit.']] ,
        ['(berapa|biaya|buat|sku)', ['Tidak Berbayar']] ,
        ['(bisa|dapat|sku|online)', ['Tidak']] ,
        ['(yang|harus|laku|jika|sku|hilang|atau|rusak)', ['Mengurus kembali ke kantor Desa']]
    ],

# RULES FOR KIA
    'kia' : [
        ['(kia)', ['Berikut pertanyaan mengenai KIA: '
                   '(Apa yang dimaksud dengan itu KIA?) (Bagaimana cara membuat KIA?) (Siapa saja yang bisa mendapatkan KIA?)']],
        ['(itu|kia)', ['KIA merupakan Kartu identitas seorang anak yang berlaku sampai usia 16 tahun dalam arti lain ini merupakan "KTP" nya anak-anak']] ,
        ['(manfaat|kia)', ['sebagai kartu identitas, sama halnya dengan Kartu Tanda Penduduk (KTP)']] ,
        ['(siapa|yang|bisa|dapat|kia)', ['namun KIA diperuntukkan bagi anak-anak yang berusia antara 0-5 tahun dan 5-17 tahun kurang satu hari']] ,
        ['(buat|kia)', ['dengan membawa Fotocopi KK, Fotocopi Akta Kelahiran dan Pasphoto 4x6(bagi yang berumur diatas 6 Tahun)']] ,
        ['(berapa|biaya|buat|kia)', ['gratis']] ,
        ['(jika|anak|hilang|dan|milik|kia)', ['Tidak ada informasi terkait hal tersebut']] ,
        ['(mana|informasi|lebih|lanjut|tentang|kia|bisa|dapat)', ['Kepala Dusun, Disdukcapil, dan Internet']] ,
        ['(anak|usia|bawah|5|tahun|wajib|milik|kia)', ['tidak diwajibkan tetapi disarankan memiliki KIA']] ,
        ['(kia|bisa|guna|untuk|naik|pesawat)', ['kurang tahu']] ,
        ['(kia|bisa|guna|untuk|buka|rekening|bank)', ['Tidak. Karena syarat pembukaan Rekening Baru harus memiliki KTP-El']]
    ],

# RULES FOR DAERAH
    'daerah' : [
        ['(mana|lokasi|daerah|sebut)', ['Desa Melati II Kecamatan Perbaungan Kabupaten Serdang Bedagai Provinsi Sumatera Utara']] ,
        ['(berapa|luas|wilayah|daerah|sebut)', ['Luas dari Desa Melati 2 yaitu 1.180 Ha']] ,
        ['(berapa|jumlah|duduk|daerah|sebut)', ['Jumlas penduduk dari Desa Melati 2 yaitu 18.231 Jiwa']] ,
        ['(batas|wilayah|daerah|sebut)', ['Sebelah Utara dengan Kelurahan Melati I, Sebelah Selatan Dengan Perkebunan, Sebelah barat Dengan Desa Citaman Jernih dan Perkebunan, Sebelah Timur dengan Desa Jatimulyo']] ,
        ['(siapa|yang|jakepala|daerah|sebut)', ['Pemimpin dari Desa Melati 2 yaitu  seorang Kepala Desa']] ,
        ['(sejarah|singkat|daerah|sebut)', ['Menurut sejarah Desa Melati II adalah perjuangan Bapak Siswuyuono, dimana tanah Desa yang sekarang dinamakan Desa Melati II antara tahun 1948-1960 terbentuklah nama Kampung Melati. Dimana waku itu Bapak Siswuyuono menaman Pohon Bunga Melati bersama masyarakat di sekitar perkampungan dan tumbuh hingga saat ini. Lambat laun Kampung Melati tersebut bertambah ramai dan sesuai dengan tuntutan dan perkembangan zaman, saat ini kampung Melati telah berubah menjadi Desa Melati, maka jelaslah asal nama Melati II adalah pemetaan wilayah antara Kelurahan Melati I dan Desa Melati II.']] ,
        ['(budaya|yang|ada|daerah|sebut)', ['Budaya dan suku dari Desa Melati 2 yaitu jawa, banjar, melayu, batak, nias']] ,
        ['(makan|khas|daerah|sebut)', ['Tidak ada makanan khas dari Desa Melati 2']] ,
        ['(tempat|wisata|yang|ada|daerah|sebut)', ['Tempat wisaya dari Desa Melati 2 yaitu  Kebun Jeruk Petik Sendiri dan Palungguhan To Joyo']] ,
        ['(adat|istiadat|yang|ada|daerah|sebut)', ['jawa, banjar, melayu, batak, nias']] ,
        ['(sistem|perintah|daerah|sebut)', ['Sistem Pemerintahan Desa Murni']] ,
        ['(sumber|dapat|daerah|sebut)', ['APBN, Daerah, Pendapatan Desa, dan Pendapatan Lain yang tidak terikat']] ,
        ['(ada|ekonomi|daerah|sebut)', ['ekonomi di Desa Melati II tergolong ekonomi yang cukup baik']] ,
        ['(potensi|ekonomi|daerah|sebut)', ['Pertanian, Peternakan, Wisata, jasa dan Perdagangan']] ,
        ['(industri|yang|ada|daerah|sebut)', ['Industri Makanan, Meubel, Pakaian']] ,
        ['(ada|didik|daerah|sebut)', ['tersedia lengkap mulai dari PAUD hingga SMA']] ,
        ['(berapa|banyak|sekolah|yang|ada|daerah|sebut)', ['secara total ada 42 tempat pendidikan']] ,
        ['(ada|fasilitas|sehat|daerah|sebut)', ['Puskesmas, Praktek Bidan, Poliklinik, Balai Pengobatan dan Apotek']] ,
        ['(berapa|banyak|rumah|sakit|yang|ada|daerah|sebut)', ['Tidak ada Rumah Sakit di Desa Melati 2']] ,
        ['(berapa|jumlah|duduk|laki|daerah|sebut)', ['Jumlah penduduk laki laki di Desa Melati 2 yaitu 8.618']] ,
        ['(berapa|jumlah|duduk|perempuan|daerah|sebut)', ['Jumlah penduduk perempuan di Desa Melati 2 yaitu 9.613']] ,
        ['(berapa|rata|usia|duduk|daerah|sebut)', ['Rata rata usia dari penduduk Desa Melati 2 yaitu 19-59 Tahun']] ,
        ['(agama|yang|anut|oleh|duduk|daerah|sebut)', ['Agama yang ada di Desa Melati 2 yaitu Islam, Kristen, Katholik, Hindu, dan Budha']] ,
        ['(suku|bangsa|yang|ada|daerah|sebut)', ['jawa, banjar, melayu, batak, nias']] ,
        ['(tingkat|padat|duduk|daerah|sebut)', ['dari 1.180 Ha Jumlah Wilayah 195 Ha merupakan Pemukiman Masyarakat']] ,
        ['(kurang|daerah|sebut)', ['Kekuarangan, Jauh dari Kawasan industri sehingga sedikit lapangan kerja']] ,
        ['(unggul|daerah|sebut)', ['Keunggulan, Memiliki Lahan Pertanian yang Luas, Jumlah Penduduk Yang Banyak, Jarak Ke Ibu Kota Kecamatan dan Ibu Kota Kabupaten tidak Jauh.']] ,
        ['(tantang|yang|hadap|daerah|sebut)', ['Tantangan bisa menjadi Lumbung Pangan dengan potensi wilayah pertanian yang cukup luas.']] ,
        ['(peluang|yang|hadap|daerah|sebut)', ['Peluang bisa menjadi Lumbung Pangan dengan potensi wilayah pertanian yang cukup luas.']] ,
        ['(rencana|bangun|daerah|sebut|masa|depan)', ['Direncanakan Desa Melati II menjadi Desa Wisata yang sejahtera dengan melibatkan warga masyarakat']]
    ]
}