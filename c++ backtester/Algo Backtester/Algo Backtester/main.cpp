#include <iostream>
#include <istream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>

#include"lib.hpp"
#include <format>






std::vector<std::vector<std::string>> getDataframe(std::string directory) 
{

    string line;
    ifstream myfile(directory);

    std::vector<std::vector<std::string>> data;


    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            //cout << line << '\n';

            std::vector<std::string> v = split(line, '\t');

            std::vector<std::string> fixed_v;

            for (const string& text : v) {
                string _text = text;
                _text.erase(std::remove(_text.begin(), _text.end(), ' '), _text.end());
                fixed_v.push_back(_text);
            }

            data.push_back(fixed_v);


        }
        myfile.close();
    }

    else {
        cout << "Unable to open file";
        
    }

    return data;

}



void executeTradeSignal(std::vector<std::vector<std::string>> data)
{

    int share_in_portfolio = 0;
    double cash_spent = 0;
    double current_cash = 0;
    double networth = 0;



    for (std::vector<std::string> i : data) {

        if (i[8] == "trading_signal") continue;

        if (std::stoi(i[8]) != 0) // trading_signal
        {
            if (std::stoi(i[8]) > 0) 
            {
                cash_spent += atof(i[1].c_str()); //Close price
                share_in_portfolio += std::stoi(i[8]);

                networth = current_cash + share_in_portfolio * atof(i[1].c_str());

                cout << std::format("bought {0} shares. Total cash spent: {1}. Current cash: {2}. Networth: {3}", std::stoi(i[8]), cash_spent, current_cash, networth) << '\n';
            }

            if (std::stoi(i[8]) < 0)
            {
                current_cash += atof(i[1].c_str()); //Close price
                share_in_portfolio += std::stoi(i[8]);  // + because the value is -1

                networth = current_cash + share_in_portfolio * atof(i[1].c_str());

                cout << std::format("sold {0} shares. Total cash spent: {1}. Current cash: {2}. Networth: {3}", abs(std::stoi(i[8])), cash_spent, current_cash, networth) << '\n';
            }

        }

    }


    cout << std::format("Final report\nCash spent: {0}\nFinal networth: {1}\nPercentage change: {2}%", cash_spent, networth, double((networth - cash_spent) / cash_spent) * 100);



}






int main()
{


    auto data = getDataframe("D:\\back up\\Programming\\Algo Backtester\\python macd strat\\MACD trading signal.csv");
    executeTradeSignal(data);


    cin.get();
    cin.get();


    return 0;


}