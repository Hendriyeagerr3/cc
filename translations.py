"""
Module untuk menangani terjemahan pesan dalam berbagai bahasa
"""

# Dictionary untuk emoji yang digunakan dalam aplikasi
EMOJIS = {
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    'cookie': '🍪',
    'lock': '🔒',
    'unlock': '🔓',
    'shell': '💰',
    'user': '👤',
    'phone': '📱',
    'email': '📧',
    'country': '🌐',
    'facebook': '👥',
    'status': '📊',
    'account': '🔑',
    'loading': '⏳',
    'summary': '📝',
    'file': '📁',
    'time': '⏰',
    'login': '🔐',
    'operation': '⚙️',
    'binds': '🔗',
    'authenticator': '🔐',
    'verification': '✓',
    'avatar': '🖼️',
    'clipboard': '📋',
    'save': '💾',
}

# Dictionary untuk terjemahan pesan error dan sebagainya
TRANSLATIONS = {
    # Bahasa Indonesia
    'id': {
        # Error messages
        'checking': 'Memeriksa',
        'prelogin_failed': '{error} {account}: Prelogin gagal',
        'login_failed': '{error} {account}: Login gagal (Password salah)',
        'account_details_failed': '{error} {account}: Gagal mengambil detail akun',
        'datadome_failed': '{error} {account}: Gagal mendapatkan cookie DataDome',
        'invalid_format': '{warning} Format tidak valid: {line}',
        'initialization_failed': '{warning} Inisialisasi gagal: {e}',
        'fetch_error': '{warning} Error mengambil data prelogin untuk {account}: {e}',
        'cookie_applied': '{info} Cookie diterapkan: {cookie_dict}',
        'using_saved_cookie': '{cookie} Menggunakan cookie tersimpan',
        'using_user_cookie': '{cookie} Menggunakan cookie dari pengguna',
        'cookie_saved': '{cookie} Cookie baru disimpan',
        'random_cookie': '{cookie} Menggunakan cookie acak dari file',
        'fresh_cookie': '{cookie} Mendapatkan cookie baru dari sesi',
        'account_initialized': '{success} Data dasar akun diambil',
        'wallet_fetched': '{success} Data wallet diambil',
        'login_history_fetched': '{success} Riwayat login diambil',
        'sensitive_ops_fetched': '{success} Operasi sensitif diambil',
        'shells_found': '{shell} Shells ditemukan di field: {key}',
        'shells_wallet': '{shell} Shells ditemukan di wallet.shell',
        'datadome_found': '{success} Cookie DataDome ditemukan: {datadome}',
        'login_success': '{success} Berhasil login: {account}',
        'ctrl_c': '{warning} Proses dihentikan oleh pengguna (Ctrl+C)',
        'showing_summary': '{info} Menampilkan ringkasan untuk akun yang telah diproses...',
        'error_processing': 'Error memproses akun: {e}',
        'combo_created': '{warning} Folder \'Combo\' dibuat. Silakan tambahkan file combo Anda di sana.',
        'no_combo_found': '{error} Tidak ada file combo ditemukan di folder Combo.',
        'invalid_selection': '{error} Pilihan tidak valid.',
        'invalid_input': '{error} Input tidak valid. Harap masukkan angka.',
        'loaded_accounts': '{success} Memuat {total_accounts} akun dari {file}',
        'cookies_required': '{warning} Cookies diperlukan untuk memulai pemeriksaan.',
        'cookies_found': '{success} Cookie yang tersimpan ditemukan!',
        'use_saved': '{info} Gunakan cookie yang tersimpan? (y/n):',
        'enter_cookie': '{info} Masukkan cookie (format: key1=value1; key2=value2):',
        'status_success': '{success} Berhasil',
        'status_failed': '{error} Gagal',
        'ctrl_c_note': '{warning} Catatan: Tekan Ctrl+C kapan saja untuk menghentikan proses. Ringkasan tetap akan ditampilkan.'
    },
    
    # Bahasa Inggris
    'en': {
        # Error messages
        'checking': 'Checking',
        'prelogin_failed': '{error} {account}: Prelogin failed',
        'login_failed': '{error} {account}: Login failed (Wrong password)',
        'account_details_failed': '{error} {account}: Failed to fetch account details',
        'datadome_failed': '{error} {account}: DataDome cookie generation failed',
        'invalid_format': '{warning} Invalid format: {line}',
        'initialization_failed': '{warning} Initialization failed: {e}',
        'fetch_error': '{warning} Error fetching prelogin data for {account}: {e}',
        'cookie_applied': '{info} Cookie applied: {cookie_dict}',
        'using_saved_cookie': '{cookie} Using saved cookie',
        'using_user_cookie': '{cookie} Using user provided cookie',
        'cookie_saved': '{cookie} New cookie saved',
        'random_cookie': '{cookie} Using random cookie from file',
        'fresh_cookie': '{cookie} Getting fresh cookie from session',
        'account_initialized': '{success} Account basic data fetched',
        'wallet_fetched': '{success} Wallet data fetched',
        'login_history_fetched': '{success} Login history fetched',
        'sensitive_ops_fetched': '{success} Sensitive operations fetched',
        'shells_found': '{shell} Shells found in field: {key}',
        'shells_wallet': '{shell} Shells found in wallet.shell',
        'datadome_found': '{success} DataDome cookie found: {datadome}',
        'login_success': '{success} Logged in: {account}',
        'ctrl_c': '{warning} Process interrupted by user (Ctrl+C)',
        'showing_summary': '{info} Showing summary for processed accounts...',
        'error_processing': 'Error processing accounts: {e}',
        'combo_created': '{warning} Created \'Combo\' folder. Please add your combo files there.',
        'no_combo_found': '{error} No combo files found in the Combo folder.',
        'invalid_selection': '{error} Invalid selection.',
        'invalid_input': '{error} Invalid input. Please enter a number.',
        'loaded_accounts': '{success} Loaded {total_accounts} accounts from {file}',
        'cookies_required': '{warning} Cookies are required to start checking.',
        'cookies_found': '{success} Saved cookies found!',
        'use_saved': '{info} Use saved cookies? (y/n):',
        'enter_cookie': '{info} Enter cookie (format: key1=value1; key2=value2):',
        'status_success': '{success} Success',
        'status_failed': '{error} Failed',
        'ctrl_c_note': '{warning} Note: Press Ctrl+C at any time to stop the process. A summary will still be displayed.'
    },
    
    # Bahasa Malaysia
    'my': {
        # Error messages
        'checking': 'Memeriksa',
        'prelogin_failed': '{error} {account}: Prelogin gagal',
        'login_failed': '{error} {account}: Login gagal (Kata laluan salah)',
        'account_details_failed': '{error} {account}: Gagal mendapatkan maklumat akaun',
        'datadome_failed': '{error} {account}: Penjanaan cookie DataDome gagal',
        'invalid_format': '{warning} Format tidak sah: {line}',
        'initialization_failed': '{warning} Inisialisasi gagal: {e}',
        'fetch_error': '{warning} Ralat mendapatkan data prelogin untuk {account}: {e}',
        'cookie_applied': '{info} Cookie diaplikasikan: {cookie_dict}',
        'using_saved_cookie': '{cookie} Menggunakan cookie tersimpan',
        'using_user_cookie': '{cookie} Menggunakan cookie dari pengguna',
        'cookie_saved': '{cookie} Cookie baru disimpan',
        'random_cookie': '{cookie} Menggunakan cookie rawak dari fail',
        'fresh_cookie': '{cookie} Mendapatkan cookie baru dari sesi',
        'account_initialized': '{success} Data asas akaun diambil',
        'wallet_fetched': '{success} Data dompet diambil',
        'login_history_fetched': '{success} Sejarah log masuk diambil',
        'sensitive_ops_fetched': '{success} Operasi sensitif diambil',
        'shells_found': '{shell} Shells dijumpai dalam bidang: {key}',
        'shells_wallet': '{shell} Shells dijumpai dalam wallet.shell',
        'datadome_found': '{success} Cookie DataDome dijumpai: {datadome}',
        'login_success': '{success} Berjaya log masuk: {account}',
        'ctrl_c': '{warning} Proses dihentikan oleh pengguna (Ctrl+C)',
        'showing_summary': '{info} Menunjukkan ringkasan untuk akaun yang telah diproses...',
        'error_processing': 'Ralat memproses akaun: {e}',
        'combo_created': '{warning} Folder \'Combo\' dibuat. Sila tambah fail combo anda di sana.',
        'no_combo_found': '{error} Tiada fail combo dijumpai dalam folder Combo.',
        'invalid_selection': '{error} Pilihan tidak sah.',
        'invalid_input': '{error} Input tidak sah. Sila masukkan nombor.',
        'loaded_accounts': '{success} Memuatkan {total_accounts} akaun dari {file}',
        'cookies_required': '{warning} Cookies diperlukan untuk mula memeriksa.',
        'cookies_found': '{success} Cookie tersimpan dijumpai!',
        'use_saved': '{info} Gunakan cookie tersimpan? (y/n):',
        'enter_cookie': '{info} Masukkan cookie (format: key1=value1; key2=value2):',
        'status_success': '{success} Berjaya',
        'status_failed': '{error} Gagal',
        'ctrl_c_note': '{warning} Nota: Tekan Ctrl+C pada bila-bila masa untuk menghentikan proses. Ringkasan masih akan dipaparkan.'
    },
    
    # Bahasa Tagalog (Filipina)
    'tl': {
        # Error messages
        'checking': 'Sinusuri',
        'prelogin_failed': '{error} {account}: Nabigo ang prelogin',
        'login_failed': '{error} {account}: Nabigo ang pag-login (Maling password)',
        'account_details_failed': '{error} {account}: Hindi makuha ang mga detalye ng account',
        'datadome_failed': '{error} {account}: Nabigo ang paggawa ng DataDome cookie',
        'invalid_format': '{warning} Hindi valid ang format: {line}',
        'initialization_failed': '{warning} Nabigo ang initialization: {e}',
        'fetch_error': '{warning} May error sa pagkuha ng prelogin data para sa {account}: {e}',
        'cookie_applied': '{info} Na-apply na ang cookie: {cookie_dict}',
        'using_saved_cookie': '{cookie} Gumagamit ng naka-save na cookie',
        'using_user_cookie': '{cookie} Gumagamit ng cookie mula sa user',
        'cookie_saved': '{cookie} Bagong cookie na-save',
        'random_cookie': '{cookie} Gumagamit ng random cookie mula sa file',
        'fresh_cookie': '{cookie} Kumukuha ng bagong cookie mula sa session',
        'account_initialized': '{success} Nakuha na ang pangunahing data ng account',
        'wallet_fetched': '{success} Nakuha na ang data ng wallet',
        'login_history_fetched': '{success} Nakuha na ang kasaysayan ng pag-login',
        'sensitive_ops_fetched': '{success} Nakuha na ang mga sensitibong operasyon',
        'shells_found': '{shell} Natagpuan ang mga Shells sa field: {key}',
        'shells_wallet': '{shell} Natagpuan ang mga Shells sa wallet.shell',
        'datadome_found': '{success} Natagpuan ang DataDome cookie: {datadome}',
        'login_success': '{success} Matagumpay na naka-login: {account}',
        'ctrl_c': '{warning} Naputol ang proseso ng user (Ctrl+C)',
        'showing_summary': '{info} Nagpapakita ng buod para sa mga na-prosesong account...',
        'error_processing': 'Error sa pagproseso ng account: {e}',
        'combo_created': '{warning} Nagawa na ang \'Combo\' folder. Mangyaring magdagdag ng iyong combo files doon.',
        'no_combo_found': '{error} Walang natagpuang combo files sa Combo folder.',
        'invalid_selection': '{error} Hindi valid ang pagpili.',
        'invalid_input': '{error} Hindi valid ang input. Mangyaring maglagay ng numero.',
        'loaded_accounts': '{success} Na-load ang {total_accounts} account mula sa {file}',
        'cookies_required': '{warning} Kinakailangan ng Cookies para magsimulang magsuri.',
        'cookies_found': '{success} Natagpuan ang naka-save na cookie!',
        'use_saved': '{info} Gamitin ang naka-save na cookie? (y/n):',
        'enter_cookie': '{info} Ilagay ang cookie (format: key1=value1; key2=value2):',
        'status_success': '{success} Tagumpay',
        'status_failed': '{error} Nabigo',
        'ctrl_c_note': '{warning} Tandaan: Pindutin ang Ctrl+C anumang oras para itigil ang proseso. Magpapakita pa rin ng buod.'
    }
}

def get_message(key, lang='id', **kwargs):
    """
    Mendapatkan pesan terjemahan dalam bahasa tertentu
    
    Args:
        key: Kunci pesan yang akan diterjemahkan
        lang: Kode bahasa ('id', 'en', 'my', 'tl')
        **kwargs: Parameter yang akan dimasukkan ke dalam pesan
    
    Returns:
        String pesan yang telah diterjemahkan
    """
    # Default ke bahasa Indonesia jika bahasa tidak tersedia
    if lang not in TRANSLATIONS:
        lang = 'id'
    
    # Dapatkan terjemahan dari dictionary
    translation = TRANSLATIONS[lang].get(key, key)
    
    # Ganti placeholder emoji dengan emoji yang sesuai
    for emoji_key, emoji_value in EMOJIS.items():
        placeholder = '{' + emoji_key + '}'
        if placeholder in translation:
            translation = translation.replace(placeholder, emoji_value)
    
    # Format pesan dengan parameter yang diberikan
    try:
        return translation.format(**kwargs)
    except KeyError as e:
        return f"Missing parameter in translation: {e}"
    except Exception as e:
        return f"Error formatting translation: {e}"