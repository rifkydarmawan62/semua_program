<?php
const PEMBARUAN_TERAKHIR = "20 November 2023";
function brute_force(string $abjad_tunggal, int $panjang_kata_sandi, string | null $kata_sandi_loop_brute_force = null, bool $loop = false) : iterable{
    if($panjang_kata_sandi <= 0 || strlen($abjad_tunggal) <= 0){
        yield "Kedua Argumen Tidak Valid!";
    }else{
        $abjad_tunggal_duplikasi = false;
        for($indeks = 0; $indeks < strlen($abjad_tunggal); ++$indeks){
            global $abjad_tunggal_duplikasi;
            if(substr_count($abjad_tunggal, $abjad_tunggal[$indeks] > 1)){
                $abjad_tunggal_duplikasi = true;
                break;
            }else{
                $abjad_tunggal_duplikasi = false;
            }
        }
        if($abjad_tunggal_duplikasi === false){
            if($loop === true && $kata_sandi_loop_brute_force !== null){
                if(strlen($kata_sandi_loop_brute_force) < $panjang_kata_sandi){
                    for($indeks = 0; $indeks < strlen($abjad_tunggal); ++$indeks){
                        $kata_sandi_sekarang = $kata_sandi_loop_brute_force . $abjad_tunggal[$indeks];
                        foreach(brute_force($abjad_tunggal, $panjang_kata_sandi, $kata_sandi_sekarang, true) as $iterator_kata_sandi){
                            yield $iterator_kata_sandi;
                        }
                    }
                }else{
                    yield $kata_sandi_loop_brute_force;
                }
            }else{
                for($digit_brute_force_saat_ini = 1; $digit_brute_force_saat_ini <= $panjang_kata_sandi; ++$digit_brute_force_saat_ini){
                    foreach(brute_force($abjad_tunggal, $digit_brute_force_saat_ini, "", true) as $iterator_kata_sandi){
                        yield $iterator_kata_sandi;
                    }
                }
            }
        }else{
            yield "Abjad duplikasi tidak diperbolehkan untuk metode peretasan brute force";
        }
    }
}
?>