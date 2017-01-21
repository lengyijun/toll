# -*- coding: utf-8 -*-
ll=[0 for i in range(9)]

for _ in range(120):
    ll[4]-=40
    ll[5]-=40
    ll[6]-=40
    if ll[4]<0:ll[4]=0
    if ll[5]<0:ll[5]=0
    if ll[6]<0:ll[6]=0

    if ll[5]<ll[4]:
        ll[5]+=0.2*ll[4]
        ll[4]-=0.2*ll[4]
    else:
        ll[4]+=0.2*ll[5]
        ll[5]-=0.2*ll[5]

    if ll[5]<ll[6]:
        ll[5]+=0.2*ll[6]
        ll[6]-=0.2*ll[6]
    else:
        ll[6]+=0.2*ll[5]
        ll[5]-=0.2*ll[5]

    ll[4]+=ll[3]
    ll[3]=0
    ll[3]=ll[2]
    ll[2]=0
    ll[2]=ll[1]
    ll[1]=0

    ll[6]+=ll[7]
    ll[7]=0
    ll[7]=ll[8]
    ll[8]=0

    ll[1]+=7
    ll[2]+=7
    ll[3]+=7
    ll[7]+=7
    ll[8]+=7

    ll[4]+=7
    ll[6]+=7

    ll[5]+=7

    for i in range(len(ll)):
        ll[i]=round(ll[i])
    print ll[1:]
