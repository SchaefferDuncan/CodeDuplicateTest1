# import numpy as np
# import matplotlib.pyplot as plt
# import astropy.units as u
# from astropy.modeling.blackbody import blackbody_lambda
# from dust_extinction.parameter_averages import F99

# define the model
# ext = F99(Rv=3.1)

# wavelengths and spectrum are 1D arrays
# wavelengths between 1000 and 30000 A
wavelengths = np.logspace(np.log10(1000), np.log10(3e4), num=1000)*u.AA
spectrum = blackbody_lambda(wavelengths, 10000*u.K)

# extinguish (redden) the spectrum
spectrum_ext = spectrum*ext.extinguish(wavelengths, Ebv=0.5)

# unextinguish (deredden) the spectrum
spectrum_noext = spectrum_ext/ext.extinguish(wavelengths, Av=1.55)

# plot the intrinsic and extinguished fluxes
fig, ax = plt.subplots()

ax.plot(wavelengths, spectrum, label='spectrum', linewidth=6, alpha=0.5)
ax.plot(wavelengths, spectrum_ext, label='spectrum_ext')
ax.plot(wavelengths, spectrum_noext, 'k', label='spectrum_noext')

ax.set_xlabel('$\lambda$ [{}]'.format(wavelengths.unit))
ax.set_ylabel('$Flux$ [{}]'.format(spectrum.unit))

ax.set_xscale('log')
ax.set_yscale('log')

ax.legend(loc='best')
plt.tight_layout()
plt.show()