#ifndef X
	#error "Define X in compile option."
#endif

#ifndef ELEM
	#error "Define ELEM in compile option."
#endif

#ifndef RANGE_MAX
	#error "Define RANGE_MAX in compile option."
#endif

#ifndef RANGE_MIN
	#error "Define RANGE_MIN in compile option."
#endif

#define Ceilings (X*X)
#define OneLine (X*(Ceilings+1)/2)

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

void MkLine(int level);
void chk_and_add(int* ar);

short int dned[Ceilings];
int ar[ELEM];
FILE* fp[(RANGE_MAX)-(RANGE_MIN)+1];

int main(int argc, char* argv[])
{
	int i;
	char s[10];
	system("rm -rf out; mkdir out");
	chdir("out");
	if(errno)
		perror("chdir: out");
	for(i=0; i<Ceilings; i++)
		dned[i]=0;
	for(i=RANGE_MIN; i<RANGE_MAX+1; i++){
		sprintf(s, "%d", i);
		fp[i-(RANGE_MIN)]=fopen(s, "w");
		if(errno)
			perror("fopen");
	}
	MkLine(0);
	for(i=RANGE_MIN; i<RANGE_MAX+1; i++)
		fclose(fp[i-(RANGE_MIN)]);
	return 0;
}

void MkLine(int level)
{
	int i;

	if(level==ELEM)
		chk_and_add(ar);
	else
		for(i=1; i<Ceilings+1; i++){
			if(dned[i-1])
				continue;
			ar[level]=i;
			dned[i-1]=1;
			MkLine(level+1);
			dned[i-1]=0;
		}
	return;
}

void chk_and_add(int* ar)
{
	int i, sum=0;

	for(i=0; i<ELEM; i++)
		sum+=ar[i];

	/*if( (sum>=OneLine-Ceilings-(Ceilings-1)) && (OneLine-1-2>=sum) ){*/
	if( (sum>=RANGE_MIN) && (RANGE_MAX>=sum) ){
		for(i=0; i<ELEM; i++)
			fprintf(fp[sum-(RANGE_MIN)], "%d ", ar[i]);
		putc('\n', fp[sum-(RANGE_MIN)]);
	}
	return;
}
