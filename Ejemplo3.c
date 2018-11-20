// This is a test
// find of a long one
// I don't care l123456789w
// I'm A87654321
/* Like at all A01064725 and some more text */
/* Let's
see
if
multiline */

proto int factorialRecursivo(int iNumero1, int iNumero2);

func int factorialRecursivo(int iNumero1, int iNumero2)
{
	int iRespuesta;
	bool bContador;

	iRespuesta = iNumero1 + iNumero2;
	bContador = FALSE;

	return iRespuesta;
}

func int fibonacci(int iNumeroFibonacci)
{
	if (iNumeroFibonacci < 2)
	{
		return 1;
	}
	return fibonacci(iNumeroFibonacci - 1) + fibonacci(iNumeroFibonacci - 2);
}

func int return3()
{
	int iArrPrueba[10];
	int iContador;
	for (iContador = 0; iContador < 10; ++iContador)
	{
		iArrPrueba[iContador] = 10 * iContador;
	}
	for (iContador = 0; iContador < 10; ++iContador)
	{
		write(iArrPrueba[iContador]);
	}
	return 3;
}

main
{
	int iParaSumar;

	iParaSumar = 8;

	write(19);
	write("some text");
	write(return3());
	write(fibonacci(read(int)));

}
