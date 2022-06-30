def anio_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

for i in (2012, 2010, 2000, 1900):
    print("El año {} es bisiesto?: {}".format(i, anio_bisiesto(i)))

#__END__