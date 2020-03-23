# for conversion from PS1 to SDSS using formula and coefficients from Tonry+12

a0_r = -.001
a1_r = 0.004
a2_r = 0.007
a0_i = -.005
a1_i = 0.011
a2_i = 0.010
a0_z = 0.013
a1_z = -.039
a2_z = -0.01


def ps1_conv_sdss(a0, a1, a2, g, r, ps1_mag): # ps1_mag = ps1_mag in band you want to calculate
    x = g - r # g and r are numpy arrays, ps1 mags
    y = a0 + a1 * x + a2 * x ** 2 # calculating correction
    sdss_mag = ps1_mag + y
    return sdss_mag
temp_zpt = 25

#example: for i-band

#sdss_i = ps1_conv_sdss(a0_i, a1_i, a2_i, ps1_g, ps1_r, ps1_i)

#m_zp_i = sdss_i - (phot_i - temp_zpt)

#print('Zpt = ' + str(np.mean(m_zp_i)) + ', err = ' + str(np.std(m_zp_i)))
