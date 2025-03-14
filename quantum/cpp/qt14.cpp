#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int get_bit(int x, int i) {
    return (x >> i) & 1;
}

void sbox(const int t[4], int z[4]) {
    int a0 = t[1] ^ t[2];
    int a1 = t[0] ^ t[1];
    int a2 = t[2] ^ t[3];
    int a3 = t[0] ^ t[2];
    int a4 = t[1] ^ t[3];
    int a5 = t[3];
    int b0 = t[0];
    int b1 = a0 ^ 1;
    int c0 = b0 & b1;
    int d0 = a0 ^ a5;
    int b2 = d0 ^ c0;
    int b3 = a1 ^ c0 ^ 1;
    int c1 = b2 & b3;
    int b4 = b3 ^ a2 ^ c1;
    int b5 = a0 ^ c1;
    int c2 = b4 & b5;
    int d1 = a3 ^ c2;
    int b6 = d1 ^ a5;
    int b7 = d0 ^ c2;
    int c3 = b6 & b7;
    int b8 = d1 ^ c0 ^ c1;
    int b9 = a1 ^ a5 ^ c1;
    int c4 = b8 & b9;
    int c5 = c2 ^ c3;
    z[0] = b2 ^ c5 ^ c4;
    z[1] = a4 ^ c2 ^ c4;
    z[2] = b4 ^ c3 ^ 1;
    z[3] = b3 ^ c5 ^ 1;
}

void x(int &x) {
	x ^= 1;
}

void cx(int &x, int &y) {
    y ^= x;
}

void ccx(int &x, int &y, int &z) {
    z ^= (x & y);
}

void QAND(int &x, int &y, int &z1, int &z2) {
	assert(z1 == 0);
	assert(z2 == 0);
	z1 = x & y;
}

void QAND_1(int &x, int &y, int &z) {
	assert(z == (x & y));
	z = 0;
}

// 9个QAND，29个CNOT
void qt14(int a[4], int d[21]) {
	cx(a[1], d[1]);
	cx(a[0], d[1]);
	cx(a[3], d[2]);
	cx(a[1], d[2]);
	cx(a[2], d[3]);
	cx(a[0], d[3]);
	cx(d[2], d[0]);
	cx(d[3], d[0]);

	QAND(d[0], d[1], d[4], d[15]);
	QAND(d[2], a[1], d[5], d[16]);
	QAND(d[3], a[0], d[6], d[17]);

	cx(d[4], d[6]);
	cx(a[2], d[6]);
	cx(d[4], d[5]);
	cx(a[2], d[5]);
	cx(a[3], d[5]);
	cx(a[3], d[2]);
	cx(a[1], d[2]);
	cx(d[6], d[2]);
	cx(a[2], d[3]);
	cx(a[0], d[3]);
	cx(d[5], d[3]);
	cx(d[0], d[1]);
	cx(a[3], a[1]);
	cx(a[2], a[0]);
	cx(d[6], d[7]);
	cx(d[5], d[7]);
	cx(d[7], d[8]);

	QAND(d[7], d[1], d[9], d[15]);
	QAND(d[6], a[3], d[10], d[16]);
	QAND(d[5], a[2], d[11], d[17]);
	QAND(d[8], d[0], d[12], d[18]);
	QAND(d[2], a[1], d[13], d[19]);
	QAND(d[3], a[0], d[14], d[20]);

	cx(d[11], d[9]);
	cx(d[11], d[10]);
	cx(d[14], d[12]);
	cx(d[14], d[13]);
}

// 9个QAND_1，29个CNOT
void qt14_1(int a[4], int d[21]) {
	cx(d[14], d[13]);
	cx(d[14], d[12]);
	cx(d[11], d[10]);
	cx(d[11], d[9]);

	QAND_1(d[3], a[0], d[14]);
	QAND_1(d[2], a[1], d[13]);
	QAND_1(d[8], d[0], d[12]);
	QAND_1(d[5], a[2], d[11]);
	QAND_1(d[6], a[3], d[10]);
	QAND_1(d[7], d[1], d[9]);

	cx(d[7], d[8]);
	cx(d[5], d[7]);
	cx(d[6], d[7]);
	cx(a[2], a[0]);
	cx(a[3], a[1]);
	cx(d[0], d[1]);
	cx(d[5], d[3]);
	cx(a[0], d[3]);
	cx(a[2], d[3]);
	cx(d[6], d[2]);
	cx(a[1], d[2]);
	cx(a[3], d[2]);
	cx(a[3], d[5]);
	cx(a[2], d[5]);
	cx(d[4], d[5]);
	cx(a[2], d[6]);
	cx(d[4], d[6]);

	QAND_1(d[3], a[0], d[6]);
	QAND_1(d[2], a[1], d[5]);
	QAND_1(d[0], d[1], d[4]);

	cx(d[3], d[0]);
	cx(d[2], d[0]);
	cx(a[0], d[3]);
	cx(a[2], d[3]);
	cx(a[1], d[2]);
	cx(a[3], d[2]);
	cx(a[0], d[1]);
	cx(a[1], d[1]);
}


// gf16_sbox = [0x0, 0x1, 0x3, 0x2, 0xf, 0xc, 0x9, 0xb, 0xa, 0x6, 0x8, 0x7, 0x5, 0xe, 0xd, 0x4]
int main() {
	for (int i = 0; i < 16; i++) {
		int t[4] = {0}, a[4] = {0}, z[4] = {0}, d[21] = {0};
		t[0] = get_bit(i, 3), t[1] = get_bit(i, 2), t[2] = get_bit(i, 1), t[3] = get_bit(i, 0);
		a[3] = get_bit(i, 3), a[2] = get_bit(i, 2), a[1] = get_bit(i, 1), a[0] = get_bit(i, 0);
		sbox(t, z);
		qt14(a, d);
		int y1 = (z[0] << 3) | (z[1] << 2) | (z[2] << 1) | z[3];
		int y2 = (d[9] << 3) | (d[10] << 2) | (d[12] << 1) | d[13];
		if (y1 != y2) {
			puts("answer doesn't match");
			exit(0);
		}
		for (int j = 15; j < 21; j++) {
			if (d[j] != 0) {
				puts("qubit neq 0, error");
				exit(0);
			}
		}
		qt14_1(a, d);
		int k = (a[3] << 3) | (a[2] << 2) | (a[1] << 1) | a[0];
		for (int j = 0; j < 21; j++) {
			if (d[j] != 0) {
				puts("can't revocer qubit");
				exit(0);
			}
		}
		if (k != i) {
			puts("can't revocer input");
			exit(0);
		}
	}
	puts("OK");
	return 0;
}