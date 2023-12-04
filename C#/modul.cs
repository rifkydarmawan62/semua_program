namespace Modul
{
    public class Teks {
        public static bool adalah_abjad_tunggal_duplikasi(string teks)
        {
            for (short indeks = 0; indeks < teks.Length; indeks++)
            {
                char a = teks[indeks];
                for (int indeks_pembanding = indeks + 1; indeks_pembanding < teks.Length; indeks_pembanding++)
                {
                    if(a == teks[indeks_pembanding])
                    {
                        return true;
                    }
                }
            }
            return false;
        }
    }
    public class Bilangan
    {
        public static bool adalah_positif(decimal angka)
        {
            return angka > 0;
        }
        public static bool adalah_negatif(decimal angka)
        {
            return angka < 0;
        }
        public static decimal kebalikan(decimal angka)
        {
            if (angka > 0)
            {
                return 0 - angka;
            }else if(angka < 0)
            {
                return angka * -1;
            }
            else
            {
                return angka;
            }
        }
        public static bool adalah_genap(long angka)
        {
            if(angka < 0)
            {
                angka *= -1;
            }
            return angka % 2 == 0;
        }
        public static bool adalah_ganjil(long angka)
        {
            if(angka < 0)
            {
                angka *= -1;
            }
            return angka % 2 != 0;
        }
    }
    public class Internet
    {
        public static bool adalah_ipv4(string alamat_ip)
        {
            alamat_ip.Trim();
            if (alamat_ip.Contains('.'))
            {
                string[] nilai_ip_array = alamat_ip.Split('.');
                if (nilai_ip_array.Length != 4)
                {
                    return false;
                }
                else
                {
                    short nilai_ip;
                    foreach (var item in nilai_ip_array)
                    {
                        if (short.TryParse(item, out nilai_ip))
                        {
                            if (nilai_ip >= 0 && nilai_ip <= 255)
                            {
                                continue;
                            }
                            else
                            {
                                return false;
                            }
                        }
                        else
                        {
                            return false;
                        }
                    }
                    return true;
                }
            }else{
                return false;
            }
        }
    }
}