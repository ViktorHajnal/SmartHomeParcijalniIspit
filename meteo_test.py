from bs4 import BeautifulSoup

xml_data = """
<Hrvatska>
    <DatumTermin>
        <Datum>03.11.2023</Datum>
        <Termin>11</Termin>
    </DatumTermin>
    <Grad autom="0">
        <GradIme>RC Bilogora</GradIme>
        <Lat>45.884</Lat>
        <Lon>17.200</Lon>
        <Podatci>
            <Temp> 12.7</Temp>
            <Vlaga>97</Vlaga>
            <Tlak> 988.5</Tlak>
            <TlakTend>-0.4</TlakTend>
            <VjetarSmjer>S</VjetarSmjer>
            <VjetarBrzina> 3.0</VjetarBrzina>
            <Vrijeme>pretežno oblačno</Vrijeme>
            <VrijemeZnak>4</VrijemeZnak>
        </Podatci>
    </Grad>
    <Grad autom="0">
        <GradIme>Bjelovar</GradIme>
        <Lat>45.910</Lat>
        <Lon>16.869</Lon>
        <Podatci>
            <Temp> 14.1</Temp>
            <Vlaga>92</Vlaga>
            <Tlak> 988.9</Tlak>
            <TlakTend>-0.5</TlakTend>
            <VjetarSmjer>SE</VjetarSmjer>
            <VjetarBrzina> 2.2</VjetarBrzina>
            <Vrijeme>pretežno oblačno</Vrijeme>
            <VrijemeZnak>4</VrijemeZnak>
        </Podatci>
    </Grad>
    <Grad autom="1">
        <GradIme>Crikvenica</GradIme>
        <Lat>45.173</Lat>
        <Lon>14.689</Lon>
        <Podatci>
            <Temp> 16.9</Temp>
            <Vlaga>66</Vlaga>
            <Tlak> 989.9</Tlak>
            <TlakTend>+2.4</TlakTend>
            <VjetarSmjer>S</VjetarSmjer>
            <VjetarBrzina> 4.2</VjetarBrzina>
            <Vrijeme>slab vjetar</Vrijeme>
            <VrijemeZnak>-</VrijemeZnak>
        </Podatci>
    </Grad>
</Hrvatska>
"""

# Parse the XML data
soup = BeautifulSoup(xml_data, 'xml')

# Find the data for "RC Bilogora"
gradovi = soup.find_all('Grad')
grad_crikvenica = []
for grad in gradovi:
    if grad.find('GradIme').text.strip() == 'Crikvenica':
        grad_crikvenica = grad

print(grad_crikvenica)