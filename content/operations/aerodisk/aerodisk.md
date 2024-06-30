---
title: "AeroDisk"
draft: false
description: "Data storage system AeroDisk notes"
---

FC commutation

№|controller|Interface
-|----------|---------
0|0         |[1][2]
-|1         |[3][4]
1|0         |[1][2][3]
-|1         |[4][5][6]
2|0         |[1][2][3]
-|1         |[4][5][6]
3|0         |[1][2][3]
-|1         |[4][5][6]

№ out|port out|№ in|port in
-----|--------|----|-------
0    |[1]     |1   |[2]
0    |[3]     |1   |[5]
     |        |    |
1    |[1]     |2   |[5]
1    |[4]     |2   |[2]
     |        |    |
2    |[1]     |3   |v2[2] v1[5]
2    |[4]     |3   |v2[5] v1[2]
