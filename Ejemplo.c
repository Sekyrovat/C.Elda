// This is a test
// find of a long one
// I don't care l123456789w
// I'm A87654321
/* Like at all A01064725 and some more text */
/* Let's
see
if
multiline */

const bool bMYTRUE = FALSE;
const int iA = 13;
const float fK = 25.0;
const char cIDENTIFICADOR = '9';
const char cPASA = 'p';
const char cREPRUEBA = 'r';
const string sMI_COMPI = "Es Hermoso";

bool bContador;
int iArrLoco[10];
int iQueHaceAlgo;
bool bMatMuyLoco[4][10];
string sArrXYZ[iA];

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
	int iTemp;
	iTemp = --iNumeroFibonacci - 1;
	return fibonacci(iNumeroFibonacci) + fibonacci(iNumeroFibonacci - 1);
}

main
{
	bool bQueHaceAlgo;
	int iParaSumar;
	int iContJ;
	char cDelSwitch;
	int iArrEnorme[100];
	cDelSwitch = 'p';

	switch (cDelSwitch)
	{
		case cPASA:
			iParaSumar = 7;
			break;
		case cREPRUEBA:
			iParaSumar = -7;
			break;
		case 't':
		case 'y':
		case 'z':
			cDelSwitch = 'j';
		default:
			iParaSumar = 6;
			break;
	}

	write(fibonacci(iParaSumar));

	bQueHaceAlgo = TRUE;
	iQueHaceAlgo = 37 * 7 / 15 + 3 * 2 + iParaSumar << 2;
	// Waza
	iQueHaceAlgo = 37 * 7 / 15 + 3 * 2 + iParaSumar; //UwU
	if (bQueHaceAlgo)
	{
		// esto hace cosas chidas
		bQueHaceAlgo = FALSE;

	} else if (5 - 3)
	{
		if (13 * 4)
		{
			iParaSumar = 5;
		}
		++iParaSumar;
	} else if (0)
	{
		bQueHaceAlgo = TRUE;
	} else //some comment
	{
		iParaSumar = 0 * 7;
	}
	iQueHaceAlgo = TRUE ? 15 + 15 ? 10 / 2.0 : 20 >> 2 : FALSE ? 30 : 40 * 12;
	iArrLoco[7] = --iArrLoco[3];


	for (iQueHaceAlgo = 0; iQueHaceAlgo < 100; ++iQueHaceAlgo)
	{
		for (iContJ = 0; iContJ < 200; ++iContJ)
		{
			iParaSumar += iQueHaceAlgo;
		}
		// some crazy stuff
		for (iContJ = 0; iContJ < 300; ++iContJ)
		{
			for (iContJ = 0; iContJ < 600; ++iContJ)
			{
				if (iContJ % 3 == 0)
				{
					iParaSumar += iQueHaceAlgo;
				} else if (iContJ % 3 == 1)
				{
					for (iContJ = 20; iContJ < 200; iContJ += 20)
					{
						iParaSumar += iQueHaceAlgo;
					}
				} else
				{
					iParaSumar += iQueHaceAlgo;
				}
			}
		}
	}

	while (iQueHaceAlgo)
	{
		--iQueHaceAlgo;
	}

	do
	{
		++iQueHaceAlgo;
	} while (iQueHaceAlgo < 15);
}
