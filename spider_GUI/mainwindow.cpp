#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QApplication>
#include <QMainWindow>
#include <cstdlib>



MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    std::system("python3.12 c:/Users/User/Desktop/web_spider/get_chapters.py");
}

