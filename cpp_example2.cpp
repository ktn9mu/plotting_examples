#include "TApplication.h"
#include "TROOT.h"
#include "TH2F.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TRandom3.h"
#include <iostream>

using namespace std;

void cpp_example2(int samples=10000){
    auto tr = new TRandom3();

    // Create a 2D Gaussian histogram
    auto hist1 = new TH2F("hist1","2D Gaussian;x;y",100,50,150,100,50,150);

    double mu = 100;
    double sigma = 6;

    for(int i=0; i<samples; i++){
        double x = tr->Gaus(mu, sigma);
        double y = tr->Gaus(mu, sigma);
        hist1->Fill(x, y);
    }

    auto tc2 = new TCanvas("c2","Canvas2",1200,900);
    tc2->Divide(2,2);

    tc2->cd(1);
    hist1->Draw("COLZ");

    // Gaussian + uniform offset background
    auto hist2 = new TH2F(*hist1);
    hist2->SetTitle("Gauss+offset;x;y");
    for(int i=0; i<samples/3; i++){
        double x = tr->Uniform(50,150);
        double y = tr->Uniform(50,150);
        hist2->Fill(x, y);
    }
    tc2->cd(2);
    hist2->Draw("COLZ");

    // Gaussian + 1/x^2 baseline background
    auto hist3 = new TH2F(*hist1);
    hist3->SetTitle("Gauss+offset2;x;y");
    TF1 *base2 = new TF1("base2","1/x/x",1,11);
    for(int i=0; i<samples*30; i++){
        double x = base2->GetRandom()*10+40;
        double y = base2->GetRandom()*10+40;
        hist3->Fill(x,y);
    }
    tc2->cd(3)->SetLogz();
    hist3->Draw("COLZ");

    // Double Gaussian
    auto hist4 = new TH2F(*hist1);
    hist4->SetTitle("Double Gaussian;x;y");
    for(int i=0; i<samples/2; i++){
        double x = tr->Gaus(mu, 20);
        double y = tr->Gaus(mu, 20);
        hist4->Fill(x,y);
    }
    tc2->cd(4);
    hist4->Draw("COLZ");

    tc2->Update();

    tc2->SaveAs("canvas2d_cpp.png");
}

int main(int argc, char **argv) {
    int nsamples=10000;
    TApplication theApp("App", &argc, argv);
    if (argc>1) nsamples=atoi(argv[1]);
    cpp_example2(nsamples);
    if (!gROOT->IsBatch()) {
        cout << "To exit, quit ROOT from the File menu of the plot (or use control-C)" << endl;
        theApp.SetIdleTimer(30,".q");
        theApp.Run(true);
    }
    return 0;
}
