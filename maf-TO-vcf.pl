#!/usr/bin/perl 
&HG19;

print "##fileformat=VCFv4.1\n";
print "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tGENO\n";
open(A, $ARGV[0]);

while (<A>) {
    chomp;
    @tmp   = split(/\t/, $_);
    
 
    $r = uc($tmp[3]);
    if ($r ne uc($tmp[4])){$v = uc($tmp[4]);} else {$v = uc($tmp[5]);}

    if ( $tmp[1] eq "MT" ){$tmp[1] = "M";}
    $chr = $tmp[1]; 
    if ( $tmp[1] !~ /000/ ){  $chr = "chr$tmp[1]"; }

    $aux = "";
    if ( $v eq "-" ){
	$v =~ s/\-/""/eg;
	    
	$aux = substr($HG19{$chr}, $tmp[2]-2, 1);
	$tmp[2] = $tmp[2]-1;
	$ALT   = "$aux$v";
	$REF   = "$aux$r";
    } 
    elsif ( $r eq "-" ) {
	$r =~  s/\-/""/eg;
	$aux = substr($HG19{$chr}, $tmp[2]-1, 1);   
	$ALT   = "$aux$v";
	$REF   = "$aux$r";

    } else {
	#$aux = substr($HG19{$chr}, $tmp[1]-1, 1);
	$ALT   = "$v"; 
	$REF   = "$r";
    }
	
    $CHROM = $chr;
    $POS   = $tmp[2];
    $ID    = "."; 
    $QUAL  = 100; 
    $FILTER= "."; 
    $aux2  = substr($tmp[6],0,12);
    $aux3  = substr($tmp[6],13,2);
    $INFO  = "VAR=$r/$v;Ncbi_Build=$tmp[0];source=TCGA;sample=$aux2;stype=$aux3";

    $GENO ="1/1:33,26:59:99:639,0,872";
    $FORMAT ="GT:AD:DP:GQ:PL";
	
    print "$CHROM\t$POS\t$ID\t$REF\t$ALT\t$QUAL\t$FILTER\t$INFO\t$FORMAT\t$GENO\n";
    
}


sub HG19 {
    my ($f);

    open(B,"/home/jorge.souza/REF/hg19.un.fa");   
    %HG19=();
    $bases=""; 
    $f=0;
    while(<B>){  
	chomp; 
	if ( $_ =~ "^>") {
	    ($nome,)=  split(/\s+/,$_);
	    $nome   =~ s/\>/""/eg;
	    #$nome   = lc($nome);
	} else {
	    $HG19{$nome} .= uc($_);
	}  	
    }
    close(B)
}
