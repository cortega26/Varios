{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Conteo9s.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNHD99gK31RzPGfAmeoNPG9",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/cortega26/Varios/blob/main/Conteo9s.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mb5mw45dOgAo",
        "outputId": "95b5e1ce-671a-4f0d-fa2a-e5c876582d72"
      },
      "source": [
        "def ceros(N):\r\n",
        "  m=str(N)\r\n",
        "  largo=len(str(N))\r\n",
        "  cant=0\r\n",
        "  cont=N\r\n",
        "  lista=[]\r\n",
        "  cont2=nonines=0\r\n",
        "  \r\n",
        "  while N > 10:\r\n",
        "    while len(str(N)) == largo:\r\n",
        "      cadena=str(N)\r\n",
        "      nueves=0\r\n",
        "      pot10=largo-2\r\n",
        "      pot9=0\r\n",
        "      if cadena[0]==\"9\":\r\n",
        "        nueves=N-9*10**(largo-1)+1\r\n",
        "        N=N-int(cadena[1::])\r\n",
        "        print(nueves,N) \r\n",
        "      while pot10>=0:\r\n",
        "        nueves+= (10**pot10) * (9**pot9)\r\n",
        "        pot10-=1\r\n",
        "        pot9+=1\r\n",
        "      #nueves=nueves*int(cadena[0])\r\n",
        "      lista.append(nueves)\r\n",
        "      N=N-10**(largo-1)\r\n",
        "    largo-=1\r\n",
        "    #print(\"primer dígito\",m[0])\r\n",
        "    print(lista)\r\n",
        "    a=sum(lista)\r\n",
        "    print(sum(lista))\r\n",
        "    print(N)\r\n",
        "  \r\n",
        "  \r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "  \r\n",
        "\r\n",
        "\r\n",
        "  while cont>0:\r\n",
        "    if \"9\" in str(cont):\r\n",
        "      #print(\"contiene 9\",cont)\r\n",
        "      cont2+=1\r\n",
        "    else:\r\n",
        "      #print(\"no contiene 9\",cont)\r\n",
        "      nonines+=1\r\n",
        "    cont-=1\r\n",
        "\r\n",
        "\r\n",
        "  print(\"El número es:\",N,\"y tiene\",largo,\"dígitos\")\r\n",
        "  print(\"cantidad 9s por algoritmo:\",cant)\r\n",
        "  print(\"nueves por conteo\",cont2,\"--- sin nueves por conteo\",nonines)\r\n",
        "\r\n",
        "ceros(99158495)\r\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "9158496 90000000\n",
            "[14375527, 5217031, 5217031, 5217031, 5217031, 5217031, 5217031, 5217031, 5217031]\n",
            "56111775\n",
            "0\n",
            "El número es: 0 y tiene 7 dígitos\n",
            "cantidad 9s por algoritmo: 0\n",
            "nueves por conteo 56111775 --- sin nueves por conteo 43046720\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}