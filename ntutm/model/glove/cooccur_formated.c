#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long array_size = 2000000; // size of chunks to shuffle individually

typedef double real;

typedef struct cooccur_rec {
    int word1;
    int word2;
    real val;
} CREC;

/* Write contents of array to binary file */
int write_chunk(CREC *array, long size, FILE *fout) {
    long i = 0;
    for(i = 0; i < size; i++) fwrite(&array[i], sizeof(CREC), 1, fout);
    return 0;
}

/* Efficient string comparison */
int scmp( char *s1, char *s2 ) {
    while(*s1 != '\0' && *s1 == *s2) {s1++; s2++;}
    return(*s1 - *s2);
}


int find_arg(char *str, int argc, char **argv) {
    int i;
    for (i = 1; i < argc; i++) {
        if(!scmp(str, argv[i])) {
            if (i == argc - 1) {
                printf("No argument given for %s\n", str);
                exit(1);
            }
            return i;
        }
    }
    return -1;
}


int main(int argc, char** argv) {
	char input_file[100];
	char output_file[100];
	int i;
	FILE *fin, *fout;
	CREC tmp;
	int voc1, voc2;
	real cooccur;
	CREC *array;
	array = malloc(sizeof(CREC) * array_size);

	if ((i = find_arg((char *)"-i", argc, argv)) > 0) strcpy(input_file, argv[i+1]);
	if ((i = find_arg((char *)"-o", argc, argv)) > 0) strcpy(output_file, argv[i+1]);


	fin = fopen(input_file, "r");
	fout = fopen(output_file, "w");

	long index = 0;

	while (fscanf(fin,"%d %d %lf",&voc1, &voc2, &cooccur) != EOF) {
		array[index].word1 = voc1;
		array[index].word2 = voc2;
		array[index].val = cooccur;
		index++;
		if (index == array_size) {
			write_chunk(array, index, fout);
			index = 0;
		}
	}
	if (index > 0) {
		write_chunk(array, index, fout);
	}
	fclose(fin);
	fclose(fout);

}




