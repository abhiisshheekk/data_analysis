chup <- data.frame(y = sample(0:100,1000000,replace=T))
chup.mean <- mean(chup$y)
chup.median <- median(chup$y)
chup.mode <- names(table(chup$y))[table(chup$y)==max(table(chup$y))]
cat("1,000,000 data:\n****************\n","Mean: ",chup.mean,"\nMedian: ",chup.median,"\nMode: ",chup.mode,fill=TRUE)
sample1 <- sample(chup$y,10000,replace=F)
nikal.aaja <- names(table(sample1)[table(sample1)==max(table(sample1))])
cat("10,000 data:\n****************\n","Mean: ",mean(sample1),"\nMedian: ",median(sample1),"\nMode: ",nikal.aaja,fill=TRUE)
l <- list()
ginti <- 10000
i <- 1
while (ginti>0) {
  l <- c(l,chup$y[i])
  i =i+5
  ginti = ginti-1
}
kaka <- unlist(l)
nikal.jaa <- names(table(kaka)[table(kaka)==max(table(kaka))])
cat("10,000 step-sized data:\n****************\n","Mean: ",mean(kaka),"\nMedian: ",median(kaka),"Mode: ",nikal.jaa,fill=TRUE)
plot(chup)
hist(chup$y)
