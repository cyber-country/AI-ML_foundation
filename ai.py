def mean(n):
    total=0
    for i in range(len(n)):
        total+=n[i]
    return total/len(n)
hours=[2,4,6,8]
scores=[40,50,60,70]
w=0
b=0
lr=0.01
while True:
    score=[]
    errors=[]
    direct=[]
    for i in range(len(hours)):
        score.append(w*hours[i]+b)
    error=[]
    for j in range(len(score)):
        error.append((scores[j]-score[j])**2)
        errors.append((score[j]-scores[j])*hours[j])
        direct.append((score[j]-scores[j]))
    dw=mean(errors)
    db=mean(direct)
    mse=mean(error)
    if mse<0.000001:
        break
    w=w-lr*dw
    b=b-lr*db
print("Final weight:", w)
print("Final bias:", b)

test_hours=10
pred=w*test_hours+b
print("Predicted score for 5 hours study:",pred)