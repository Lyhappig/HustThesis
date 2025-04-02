#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

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

// 恢复前4个比特
// 9个QAND，9个QAND_1，56个CNOT
void qt14(int a[4], int b[4], int c[4], int d[28]) {
    cx(a[2], d[6]);
    cx(a[0], d[6]);
    cx(b[2], d[7]);
    cx(b[0], d[7]);
    cx(a[1], d[8]);
    cx(a[0], d[8]);
    cx(b[1], d[9]);
    cx(b[0], d[9]);
    cx(a[3], d[10]);
    cx(a[1], d[10]);
    cx(b[3], d[11]);
    cx(b[1], d[11]);
    cx(d[10], d[4]);
    cx(d[6], d[4]);
    cx(d[11], d[5]);
    cx(d[7], d[5]);
    cx(a[3], d[12]);
    cx(a[2], d[12]);
    cx(b[3], d[13]);
    cx(b[2], d[13]);
// begin
    QAND(d[4], d[5], d[3], d[19]);
    QAND(d[6], d[7], d[2], d[20]);
    QAND(d[8], d[9], d[1], d[21]);
    QAND(d[12], d[13], d[0], d[22]);
    QAND(d[10], d[11], d[14], d[23]);
    QAND(a[0], b[0], d[15], d[24]);
    QAND(a[1], b[1], d[16], d[25]);
    QAND(a[2], b[2], d[17], d[26]);
    QAND(a[3], b[3], d[18], d[27]);
	cx(d[0], c[0]);
	cx(d[1], c[1]);
	cx(d[2], c[2]);
	cx(d[3], c[3]);
// end
    cx(d[2], c[3]);
    cx(d[1], c[3]);
    cx(d[15], c[3]);
    cx(d[14], c[2]);
    cx(d[15], c[2]);
    cx(d[16], c[2]);
    cx(d[0], c[1]);
    cx(d[15], c[1]);
    cx(d[18], c[1]);
    cx(d[15], c[0]);
    cx(d[16], c[0]);
    cx(d[17], c[0]);
// begin
    QAND_1(d[12], d[13], d[0]);
	QAND_1(d[8], d[9], d[1]);
	QAND_1(d[6], d[7], d[2]);
	QAND_1(d[4], d[5], d[3]);
    QAND_1(a[3], b[3], d[18]);
    QAND_1(a[2], b[2], d[17]);
    QAND_1(a[1], b[1], d[16]);
    QAND_1(a[0], b[0], d[15]);
    QAND_1(d[10], d[11], d[14]);
// end
    cx(b[3], d[13]);
    cx(b[2], d[13]);
    cx(a[3], d[12]);
    cx(a[2], d[12]);
    cx(d[11], d[5]);
    cx(d[7], d[5]);
    cx(d[10], d[4]);
    cx(d[6], d[4]);
    cx(b[3], d[11]);
    cx(b[1], d[11]);
    cx(a[3], d[10]);
    cx(a[1], d[10]);
    cx(b[1], d[9]);
    cx(b[0], d[9]);
    cx(a[1], d[8]);
    cx(a[0], d[8]);
    cx(b[2], d[7]);
    cx(b[0], d[7]);
    cx(a[2], d[6]);
    cx(a[0], d[6]);
}

int main() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int a[4] = { (i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1, (i >> 3) & 1 };
            int b[4] = { (j >> 0) & 1, (j >> 1) & 1, (j >> 2) & 1, (j >> 3) & 1 };
			int c[4] = {0};
            int d1[28] = {0};
            int n = 28;
            qt14(a, b, c, d1);

            for (int k = 0; k < 4; k++) {
                int expected_a = (i >> k) & 1;
                int expected_b = (j >> k) & 1;
                if (a[k] != expected_a) {
                    printf("output X not match\n");
                    return 0;
                }
                if (b[k] != expected_b) {
                    printf("output Y not match\n");
                    return 0;
                }
            }

            int d2[4] = {0};
            d2[3] = ((a[3] ^ a[2] ^ a[1] ^ a[0]) & (b[3] ^ b[2] ^ b[1] ^ b[0])) ^ ((a[2] ^ a[0]) & (b[2] ^ b[0])) ^ ((a[1] ^ a[0]) & (b[1] ^ b[0])) ^ (a[0] & b[0]);
            d2[2] = ((a[3] ^ a[1]) & (b[3] ^ b[1])) ^ ((a[2] ^ a[0]) & (b[2] ^ b[0])) ^ (a[1] & b[1]) ^ (a[0] & b[0]);
            d2[1] = ((a[3] ^ a[2]) & (b[3] ^ b[2])) ^ (a[3] & b[3]) ^ ((a[1] ^ a[0]) & (b[1] ^ b[0])) ^ (a[0] & b[0]);
            d2[0] = ((a[3] ^ a[2]) & (b[3] ^ b[2])) ^ (a[2] & b[2]) ^ (a[1] & b[1]) ^ (a[0] & b[0]);

            for (int k = 0; k < 4; k++) {
                if (c[k] != d2[k]) {
                    printf("answer not match\n");
                    return 0;
                }
            }

			for (int k = 0; k < n; k++) {
				if (d1[k] != 0) {
					printf("can't recover other bits\n");
                    return 0;
				}
			}
        }
    }
    printf("OK\n");
    return 0;
}