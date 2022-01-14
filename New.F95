! prog.f95
 
function poli (X, Y, N)
real(8), dimension(N) :: X, Y
integer N
real*8 poli, s
integer i
s = 0.0
do i = 1, N-1
    s = s + X(i)*Y(i+1)-X(i+1)*Y(i)
end do
s = s + X(N)*Y(1)-X(1)*Y(N)
poli = 0.5*ABS(s)
end
 
program prog
integer N, i
real(8), dimension(:), allocatable :: X, Y
real(8) :: poli, s
write (*,'(" N = "$)')
read (*,*) N
allocate (X(N), Y(N))
do i=1,N
    write (*,'("vertex #"I3 " = "$)') i
    read (*,*) X(i), Y(i)
end do
s=poli(X, Y, N) 
write (*,*) s 
deallocate (X, Y)
end
