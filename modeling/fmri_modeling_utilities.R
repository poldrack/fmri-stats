# function to generate a boxcar design
make_boxcar_design = function(ntp,block_length) {
	design = array(0,dim=ntp)
	ctr=1
	cond=FALSE
	for (i in 1:ntp) {
		if (ctr > block_length) {
			ctr=1
			cond=!cond
			}
		if (cond) design[i]=1
		ctr = ctr + 1
		}
	return(design)
}

# function to generate SPM hemodynamic response function
# ported from spm_hrf.m in the SPM distribution
# RT = repetition time, i.e. resolution of HRF
spm_hrf <- function(RT=1.0) {
	p = c(6,16,1,1,6,0, 32);
	fMRI_T = 16;
	
	dt    = RT/fMRI_T;
	u     = seq(0,p[7]/dt) - p[6]/dt;
	#pgamma(1,1,scale=1,lower.tail=FALSE)
	hrf   = dgamma(u,p[1]/p[3],dt/p[3]) - dgamma(u,p[2]/p[4],dt/p[4])/p[5];
	hrf   = hrf[seq(0,p[7]/RT)*fMRI_T + 1];
	hrf   = t(hrf)/sum(hrf);
	return(array(hrf))
}

#convolve design with hemodynamic response
hrf_conv <- function(sf,TR=1.0) {

        hrf=spm_hrf(TR);
        new_sf=array(0,dim=length(sf)+length(hrf)-1)
        new_sf[length(hrf):length(new_sf)]=sf;
        cf=filter(new_sf,hrf,method="convolution",sides=1);
        csf=cf[length(hrf):(length(hrf)+length(sf)-1)]
		return(csf)
}

get_dct <- function(ntp,K=3,standardize=TRUE) {
	C=matrix(NA,nrow=ntp,ncol=K)
	n=c(0:(ntp-1))
	for (k in 1:K) {
		C[,k]=sqrt(2/ntp)*cos(pi*(2*n+1)*(k)/(2*ntp))
    if (standardize) {
       # standardize to (-1,1)
       C[,k]=C[,k]*(1/max(abs(range(C[,k]))))
     }
		}
	return(C)
}

generate_ar1wn_data = function(X, beta,ar1_param=0.3,whitenoise_sd=0.5) {
	# simulate some AR1 noise
  if (ar1_param>0) {
	  noise=arima.sim(n=dim(X)[1],list(ar=ar1_param),sd=whitenoise_sd)
  } else {noise=rnorm(dim(X)[1])*whitenoise_sd}
  
	# generate data 
	data = X%*%beta + noise
	
	return(data)
	}

generate_ar1_covariance = function(rho,ntp) {
	# with unit covariance (sigma)
	x <- diag(ntp)
	x <- rho^abs(row(x)-col(x))
	return(x)
}



