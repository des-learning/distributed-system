Thread memungkinkan sebuah proses untuk memiliki lebih dari _execution path_ yang dijalankan secara serentak (secara
paralel maupun _multiplexing_).

Implementasi CPython sekarang ini tidak memberikan manfaat yang maksimum. Ini dikarenakan implementasi CPython yang
menggunakan GIL (Global Interpreter Lock).

Penggunaan _thread_ di CPython untuk task yang _CPU Bound_ tidak memperoleh peningkatan kinerja karena proses python
tidak dapat menjalankan _thread_ pada banyak CPU walaupun di-sistem terdapat lebih dari 1 cpu. Sedangkan proses python
yang _I/O Bound_ dapat mengefisienkan eksekusi karena _thread_ yang sedang menunggu operasi _I/O_ dapat melepaskan
CPU untuk digunakan oleh _thread_ lain. Batasan ini cuma berlaku untuk bahasa atau _runtime_ yang menggunakan GIL.

Untuk memaksimalkan utilitas CPU pada python, _thread_ dapat digantikan dengan _multiprocessing_.
Fungsi _multiprocessing_ mirip dengan _thread_ tapi dengan menggantikan _thread_ dengan proses-proses python. Dengan
menggunakan proses batasan yang diakibatkan oleh GIL tidak lagi berpengaruh.

Konsekuensi penggunaan proses untuk menggantikan _thread_ adalah _concurrent task_ pada python dapat memaksimalkan
penggunaan cpu, tetapi karena berjalan pada proses yang terpisah, kebutuhan memory, proses _context switch_ dan
komunikasi/sinkronisasi antar proses lebih _costly_ dibandingkan dengan menggunakan _thread_.

Proses dan _thread_ merupakan layanan yang di-_manage_ oleh sistem operasi. OS melakukan penjadwalan kapan
proses/_thread_ dapat menggunakan cpu. Dan setiap cpu berpindah dari satu proses/_thread_ ke proses/_thread_ lain ada
_context switch_. Untuk lebih memaksimalkan pengunaan cpu dan mengurangi _context switch_ dikembangkan _thread_ yang
lebih _lightweight_, yang dikelola oleh proses itu sendiri, _thread_ ini disebut _green thread_ atau _virtual thread_.