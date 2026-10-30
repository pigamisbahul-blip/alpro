import java.util.ArrayList;
import java.util.List;

// =========================================================================
// 1. INTERFACE (Kontrak Pembayaran)
// =========================================================================
interface Pembayaran {
    void prosesPembayaran(double jumlah);
    // Overloading method pada interface/kelas
    void prosesPembayaran(double jumlah, double diskon);
}

class QRIS implements Pembayaran {
    private String nmQRIS;

    public QRIS(String nmQRIS) {
        this.nmQRIS = nmQRIS;
    }

    @Override
    public void prosesPembayaran(double jumlah) {
        System.out.println("[QRIS] Pembayaran sebesar Rp" + jumlah + " berhasil via QRIS (" + nmQRIS + ")");
    }

    @Override
    public void prosesPembayaran(double jumlah, double diskon) {
        double total = jumlah - diskon;
        System.out.println("[QRIS] Dipotong diskon Rp" + diskon + ". Total bayar: Rp" + total + " via QRIS (" + nmQRIS + ")");
    }
}

class Tunai implements Pembayaran {
    @Override
    public void prosesPembayaran(double jumlah) {
        System.out.println("[Tunai] Pembayaran sebesar Rp" + jumlah + " diterima secara tunai.");
    }

    @Override
    public void prosesPembayaran(double jumlah, double diskon) {
        double total = jumlah - diskon;
        System.out.println("[Tunai] Dipotong diskon Rp" + diskon + ". Total bayar: Rp" + total + " secara tunai.");
    }
}

// =========================================================================
// 2. ABSTRACT CLASS & ENCAPSULATION (Cetak Biru Konsol)
// =========================================================================
abstract class KonsolPS {
    private String idKonsol;
    private String namaKonsol;
    private double hargaPerJam;

    public KonsolPS(String idKonsol, String namaKonsol, double hargaPerJam) {
        this.idKonsol = idKonsol;
        this.namaKonsol = namaKonsol;
        this.hargaPerJam = hargaPerJam;
    }

    // Encapsulation: Getter & Setter
    public String getIdKonsol() { return idKonsol; }
    public String getNamaKonsol() { return namaKonsol; }
    public double getHargaPerJam() { return hargaPerJam; }

    public void setHargaPerJam(double hargaPerJam) {
        if (hargaPerJam > 0) {
            this.hargaPerJam = hargaPerJam;
        } else {
            System.out.println("Harga harus lebih dari 0!");
        }
    }

    public void tampilkanInfo() {
        System.out.println("ID: " + idKonsol + " | Unit: " + namaKonsol + " | Tarif: Rp" + hargaPerJam + "/jam");
    }

    // Abstract Method
    public abstract double hitungBiaya(int jam);
}

// =========================================================================
// 3. INHERITANCE & OVERRIDING (Subclass Konsol)
// =========================================================================
class PS4 extends KonsolPS {
    public PS4(String idKonsol, String namaKonsol, double hargaPerJam) {
        super(idKonsol, namaKonsol, hargaPerJam);
    }

    @Override
    public double hitungBiaya(int jam) {
        return getHargaPerJam() * jam; // Tarif standar
    }
}

class PS5 extends KonsolPS {
    private boolean includeVR;

    public PS5(String idKonsol, String namaKonsol, double hargaPerJam, boolean includeVR) {
        super(idKonsol, namaKonsol, hargaPerJam);
        this.includeVR = includeVR;
    }

    @Override
    public double hitungBiaya(int jam) {
        double total = getHargaPerJam() * jam;
        if (includeVR) {
            total += (10000 * jam); // Tambahan Rp10.000/jam jika memakai VR
        }
        return total;
    }
}

// =========================================================================
// 4. RELASI AGREGASI & KOMPOSISI
// =========================================================================
// Class Pelanggan (Agregasi - Bisa berdiri sendiri tanpa transaksi)
class Pelanggan {
    private String nama;
    private String noHp;

    public Pelanggan(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
    }

    public String getNama() { return nama; }
    public String getNoHp() { return noHp; }
}

// Class Nota (Komposisi - Dibuat langsung di dalam SewaSession & terikat penuh)
class Nota {
    private String kodeNota;

    public Nota(String kodeNota) {
        this.kodeNota = kodeNota;
    }

    public void cetakHeader() {
        System.out.println("==========================================");
        System.out.println("          RENTAL PS MANIA - NOTA " + kodeNota);
        System.out.println("==========================================");
    }
}

// Class Transaksi Sewa (Asosiasi, Agregasi, & Komposisi)
class SewaSession {
    private Pelanggan pelanggan; // Agregasi
    private KonsolPS konsol;     // Asosiasi / Polymorphism
    private Nota nota;           // Komposisi
    private int durasiJam;

    public SewaSession(Pelanggan pelanggan, KonsolPS konsol, int durasiJam, String kodeNota) {
        this.pelanggan = pelanggan;
        this.konsol = konsol;
        this.durasiJam = durasiJam;
        // Komposisi: Objek Nota diinstansiasi langsung di dalam constructor
        this.nota = new Nota(kodeNota);
    }

    public void prosesSewa(Pembayaran metodePembayaran, double diskon) {
        nota.cetakHeader();
        System.out.println("Pelanggan : " + pelanggan.getNama() + " (" + pelanggan.getNoHp() + ")");
        System.out.print("Konsol    : ");
        konsol.tampilkanInfo();
        System.out.println("Durasi    : " + durasiJam + " Jam");

        double totalBiaya = konsol.hitungBiaya(durasiJam);
        System.out.println("Subtotal  : Rp" + totalBiaya);
        
        // Polymorphism pada interface Pembayaran
        if (diskon > 0) {
            metodePembayaran.prosesPembayaran(totalBiaya, diskon);
        } else {
            metodePembayaran.prosesPembayaran(totalBiaya);
        }
        System.out.println("==========================================\n");
    }
}

// =========================================================================
// 5. MAIN CLASS (Pengujian Program)
// =========================================================================
public class MainRentalPS {
    public static void main(String[] args) {
        System.out.println("=== SISTEM MANAJEMEN RENTAL PLAYSTATION ===\n");

        // 1. Inisialisasi Objek Pelanggan (Agregasi)
        Pelanggan p1 = new Pelanggan("Piga Misbahul", "08123456789");
        Pelanggan p2 = new Pelanggan("Andi", "08987654321");

        // 2. Polymorphism Array pada Abstract Class KonsolPS
        KonsolPS[] daftarKonsol = new KonsolPS[2];
        daftarKonsol[0] = new PS4("PS4-01", "PlayStation 4 Slim", 8000);
        daftarKonsol[1] = new PS5("PS5-01", "PlayStation 5 + VR", 15000, true);

        // 3. Opsi Metode Pembayaran (Interface)
        Pembayaran bayarQris = new QRIS("RentalPS_Cirebon");
        Pembayaran bayarTunai = new Tunai();

        // 4. Simulasi Transaksi 1 (Sewa PS4 oleh Piga, Bayar QRIS + Diskon)
        SewaSession sewa1 = new SewaSession(p1, daftarKonsol[0], 3, "N-001");
        sewa1.prosesSewa(bayarQris, 2000); // Durasi 3 jam * 8000 = 24000 - 2000 diskon

        // 5. Simulasi Transaksi 2 (Sewa PS5 oleh Andi, Bayar Tunai Tanpa Diskon)
        SewaSession sewa2 = new SewaSession(p2, daftarKonsol[1], 2, "N-002");
        sewa2.prosesSewa(bayarTunai, 0);   // Durasi 2 jam * (15000 + 10000 VR) = 50000
    }
}
