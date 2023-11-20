<?php
const PEMBARUAN_TERAKHIR = "20 November 2023";
function abjad_tunggal_duplikasi(string $string): bool{
    for($indeks = 0; $indeks < strlen($string); ++$indeks){
        if(substr_count($string, $string[$indeks]) > 1){
            return true;
        }
    }
    return false;
}
?>