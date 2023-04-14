{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6a395d49",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9999b7c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\bhask\\Desktop\\DATA SCIENCE AND ANALYTICS\\Internship_Inno\\DATA_ANALYSIS_EDA\\laptop_details.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "dfea6110",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Rating</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>4.2</td>\n",
       "      <td>₹36,990</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>4.2</td>\n",
       "      <td>₹39,990</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>4.3</td>\n",
       "      <td>₹32,990</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>4.4</td>\n",
       "      <td>₹49,990</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>4.4</td>\n",
       "      <td>₹49,990</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product  Rating      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...     4.2  ₹36,990   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...     4.2  ₹39,990   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...     4.3  ₹32,990   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...     4.4  ₹49,990   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...     4.4  ₹49,990   \n",
       "\n",
       "                                             Feature  \n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...  \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...  \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...  \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...  \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...  "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a4bbd5da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>581.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.321170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.282872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Rating\n",
       "count  581.000000\n",
       "mean     4.321170\n",
       "std      0.282872\n",
       "min      3.000000\n",
       "25%      4.200000\n",
       "50%      4.300000\n",
       "75%      4.500000\n",
       "max      5.000000"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "9090ed55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 720 entries, 0 to 719\n",
      "Data columns (total 4 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   Product  720 non-null    object \n",
      " 1   Rating   581 non-null    float64\n",
      " 2   MRP      720 non-null    object \n",
      " 3   Feature  720 non-null    object \n",
      "dtypes: float64(1), object(3)\n",
      "memory usage: 22.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "d5b9d9cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Product      0\n",
       "Rating     139\n",
       "MRP          0\n",
       "Feature      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "4b81ed3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop('Rating', axis = 1, inplace = True\n",
    "       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "4ff13a37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>₹36,990</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>₹39,990</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>₹32,990</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>₹49,990</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>₹49,990</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  ₹36,990   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  ₹39,990   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  ₹32,990   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  ₹49,990   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  ₹49,990   \n",
       "\n",
       "                                             Feature  \n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...  \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...  \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...  \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...  \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "720d853a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 720 entries, 0 to 719\n",
      "Data columns (total 3 columns):\n",
      " #   Column   Non-Null Count  Dtype \n",
      "---  ------   --------------  ----- \n",
      " 0   Product  720 non-null    object\n",
      " 1   MRP      720 non-null    object\n",
      " 2   Feature  720 non-null    object\n",
      "dtypes: object(3)\n",
      "memory usage: 17.0+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "639e1a1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "76b6c416",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "4ba66da9",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'float' object has no attribute 'replace'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[1;32mIn [71]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMRP\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mMRP\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mapply\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43;01mlambda\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mx\u001b[49m\u001b[43m \u001b[49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreplace\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m₹\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreplace\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m,\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mastype(\u001b[38;5;28mfloat\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py:4433\u001b[0m, in \u001b[0;36mSeries.apply\u001b[1;34m(self, func, convert_dtype, args, **kwargs)\u001b[0m\n\u001b[0;32m   4323\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mapply\u001b[39m(\n\u001b[0;32m   4324\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m   4325\u001b[0m     func: AggFuncType,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   4328\u001b[0m     \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs,\n\u001b[0;32m   4329\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m DataFrame \u001b[38;5;241m|\u001b[39m Series:\n\u001b[0;32m   4330\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m   4331\u001b[0m \u001b[38;5;124;03m    Invoke function on values of Series.\u001b[39;00m\n\u001b[0;32m   4332\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   4431\u001b[0m \u001b[38;5;124;03m    dtype: float64\u001b[39;00m\n\u001b[0;32m   4432\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m-> 4433\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mSeriesApply\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconvert_dtype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mapply\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\apply.py:1082\u001b[0m, in \u001b[0;36mSeriesApply.apply\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1078\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mf, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m   1079\u001b[0m     \u001b[38;5;66;03m# if we are a string, try to dispatch\u001b[39;00m\n\u001b[0;32m   1080\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapply_str()\n\u001b[1;32m-> 1082\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mapply_standard\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\apply.py:1137\u001b[0m, in \u001b[0;36mSeriesApply.apply_standard\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1131\u001b[0m         values \u001b[38;5;241m=\u001b[39m obj\u001b[38;5;241m.\u001b[39mastype(\u001b[38;5;28mobject\u001b[39m)\u001b[38;5;241m.\u001b[39m_values\n\u001b[0;32m   1132\u001b[0m         \u001b[38;5;66;03m# error: Argument 2 to \"map_infer\" has incompatible type\u001b[39;00m\n\u001b[0;32m   1133\u001b[0m         \u001b[38;5;66;03m# \"Union[Callable[..., Any], str, List[Union[Callable[..., Any], str]],\u001b[39;00m\n\u001b[0;32m   1134\u001b[0m         \u001b[38;5;66;03m# Dict[Hashable, Union[Union[Callable[..., Any], str],\u001b[39;00m\n\u001b[0;32m   1135\u001b[0m         \u001b[38;5;66;03m# List[Union[Callable[..., Any], str]]]]]\"; expected\u001b[39;00m\n\u001b[0;32m   1136\u001b[0m         \u001b[38;5;66;03m# \"Callable[[Any], Any]\"\u001b[39;00m\n\u001b[1;32m-> 1137\u001b[0m         mapped \u001b[38;5;241m=\u001b[39m \u001b[43mlib\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmap_infer\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1138\u001b[0m \u001b[43m            \u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1139\u001b[0m \u001b[43m            \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m  \u001b[49m\u001b[38;5;66;43;03m# type: ignore[arg-type]\u001b[39;49;00m\n\u001b[0;32m   1140\u001b[0m \u001b[43m            \u001b[49m\u001b[43mconvert\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mconvert_dtype\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1141\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1143\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(mapped) \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(mapped[\u001b[38;5;241m0\u001b[39m], ABCSeries):\n\u001b[0;32m   1144\u001b[0m     \u001b[38;5;66;03m# GH#43986 Need to do list(mapped) in order to get treated as nested\u001b[39;00m\n\u001b[0;32m   1145\u001b[0m     \u001b[38;5;66;03m#  See also GH#25959 regarding EA support\u001b[39;00m\n\u001b[0;32m   1146\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m obj\u001b[38;5;241m.\u001b[39m_constructor_expanddim(\u001b[38;5;28mlist\u001b[39m(mapped), index\u001b[38;5;241m=\u001b[39mobj\u001b[38;5;241m.\u001b[39mindex)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\lib.pyx:2870\u001b[0m, in \u001b[0;36mpandas._libs.lib.map_infer\u001b[1;34m()\u001b[0m\n",
      "Input \u001b[1;32mIn [71]\u001b[0m, in \u001b[0;36m<lambda>\u001b[1;34m(x)\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMRP\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMRP\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mapply(\u001b[38;5;28;01mlambda\u001b[39;00m x : \u001b[43mx\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreplace\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m₹\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m.\u001b[39mreplace(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m))\u001b[38;5;241m.\u001b[39mastype(\u001b[38;5;28mfloat\u001b[39m)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'float' object has no attribute 'replace'"
     ]
    }
   ],
   "source": [
    "df['MRP'] = df['MRP'].apply(lambda x : x.replace('₹', '').replace(',', '')).astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "00c37bf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 421 entries, 0 to 719\n",
      "Data columns (total 3 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   Product  421 non-null    object \n",
      " 1   MRP      421 non-null    float64\n",
      " 2   Feature  421 non-null    object \n",
      "dtypes: float64(1), object(2)\n",
      "memory usage: 13.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f020226",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "462fa03a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "      <th>Brand_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>36990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>39990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>32990.0</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "      <td>HP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  36990.0   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  39990.0   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  32990.0   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  49990.0   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  49990.0   \n",
       "\n",
       "                                             Feature Brand_name  \n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo  \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo  \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...       ASUS  \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...         HP  \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...       ASUS  "
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Brand_name\"] = df[\"Product\"].apply(lambda x: x.split(\" \")[0])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "35f44419",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer',\n",
       "       'MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio',\n",
       "       'GIGABYTE', 'Nokia', 'ALIENWARE'], dtype=object)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Brand_name'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "10e2facd",
   "metadata": {},
   "outputs": [],
   "source": [
    "re_ram_type = r'(DDR[0-9L]*|LPDDR[0-9X]*)'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "513619d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RAM_type\n",
    "def extract_ram_type(text):\n",
    "    match = re.search(re_ram_type, text, re.IGNORECASE)\n",
    "    if match:\n",
    "        return match.group(0)\n",
    "    else:\n",
    "        return None\n",
    "df['RAM_Type'] = df['Feature'].apply(extract_ram_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "655e2da1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RAM_size\n",
    "df['RAM_Size'] = df['Feature'].apply(lambda x: int(re.findall(r'\\d+', x.split('DDR')[0])[-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "5fad4b8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>RAM_Size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>36990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>39990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>32990.0</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "      <td>HP</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  36990.0   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  39990.0   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  32990.0   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  49990.0   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  49990.0   \n",
       "\n",
       "                                             Feature Brand_name RAM_Type  \\\n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...         HP     DDR4   \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "\n",
       "   RAM_Size  \n",
       "0         8  \n",
       "1         8  \n",
       "2         8  \n",
       "3         8  \n",
       "4         8  "
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "8c26691b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Storage_size\n",
    "df[\"Storage_size\"] = df['Feature'].apply(lambda x: int(re.findall(r'\\d+', x.split('SSD')[0])[-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "b5e306a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Storage_type\n",
    "df[\"Storage_type\"] = df['Product'].apply(lambda x: \"HDD\" if 'HDD'in x else \"SSD\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "f02642e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Operating_SYstem_type\n",
    "df['OS_Type'] = df['Feature'].apply(lambda x: 'Windows' if 'Windows' in x else'Mac OS' if 'Mac OS' in x else 'Others')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "2ac4ec90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>36990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>256</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>39990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>32990.0</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "      <td>HP</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  36990.0   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  39990.0   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  32990.0   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  49990.0   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  49990.0   \n",
       "\n",
       "                                             Feature Brand_name RAM_Type  \\\n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...         HP     DDR4   \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "\n",
       "   RAM_Size  Storage_size Storage_type  OS_Type  \n",
       "0         8           256          SSD  Windows  \n",
       "1         8           512          SSD  Windows  \n",
       "2         8           512          SSD  Windows  \n",
       "3         8           512          SSD  Windows  \n",
       "4         8           512          SSD  Windows  "
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "f94578ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Processor_type\n",
    "reg= r'^(?:AMD|Intel|M1|Apple)[\\s\\w]+Processor'\n",
    "df['Processor Type']=df['Feature'].apply(lambda x : re.findall(reg, x))\n",
    "df['Processor Type']=df['Processor Type'].apply(lambda x : ''.join(x))\n",
    "df['Processor Type']=df['Processor Type'].apply(lambda x: x.replace(\" Processor\", \"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "2453fe3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "      <th>Processor Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>36990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>256</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>39990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>32990.0</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "      <td>HP</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  36990.0   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  39990.0   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  32990.0   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  49990.0   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  49990.0   \n",
       "\n",
       "                                             Feature Brand_name RAM_Type  \\\n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...         HP     DDR4   \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "\n",
       "   RAM_Size  Storage_size Storage_type  OS_Type         Processor Type  \n",
       "0         8           256          SSD  Windows          Intel Core i3  \n",
       "1         8           512          SSD  Windows          Intel Core i3  \n",
       "2         8           512          SSD  Windows          Intel Core i3  \n",
       "3         8           512          SSD  Windows  AMD Ryzen 5 Hexa Core  \n",
       "4         8           512          SSD  Windows          Intel Core i5  "
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "3feb594c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Processor_Brand\n",
    "def extract_processor_brand(text):\n",
    "    if re.search(r\"intel\", text, re.IGNORECASE):\n",
    "        return \"Intel\"\n",
    "    elif re.search(r\"amd\", text, re.IGNORECASE):\n",
    "        return \"AMD\"\n",
    "    else:\n",
    "        return \"Others\"\n",
    "\n",
    "\n",
    "df['Processor'] = df['Feature'].apply(extract_processor_brand)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "099eb882",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Intel     272\n",
       "AMD       129\n",
       "Others     20\n",
       "Name: Processor, dtype: int64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Processor'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "6ec4aa6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Intel', 'AMD', 'Others'], dtype=object)"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Processor.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "a44de411",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>MRP</th>\n",
       "      <th>Feature</th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "      <th>Processor Type</th>\n",
       "      <th>Processor</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...</td>\n",
       "      <td>36990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>256</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>39990.0</td>\n",
       "      <td>Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>Lenovo</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>32990.0</td>\n",
       "      <td>Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i3</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...</td>\n",
       "      <td>HP</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>AMD Ryzen 5 Hexa Core</td>\n",
       "      <td>AMD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>49990.0</td>\n",
       "      <td>Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...</td>\n",
       "      <td>ASUS</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>8</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Product      MRP  \\\n",
       "0  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/256 ...  36990.0   \n",
       "1  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...  39990.0   \n",
       "2  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...  32990.0   \n",
       "3  HP Pavilion Ryzen 5 Hexa Core AMD R5-5600H - (...  49990.0   \n",
       "4  ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...  49990.0   \n",
       "\n",
       "                                             Feature Brand_name RAM_Type  \\\n",
       "0  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "1  Intel Core i3 Processor (11th Gen)8 GB DDR4 RA...     Lenovo     DDR4   \n",
       "2  Intel Core i3 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "3  AMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64...         HP     DDR4   \n",
       "4  Intel Core i5 Processor (10th Gen)8 GB DDR4 RA...       ASUS     DDR4   \n",
       "\n",
       "   RAM_Size  Storage_size Storage_type  OS_Type         Processor Type  \\\n",
       "0         8           256          SSD  Windows          Intel Core i3   \n",
       "1         8           512          SSD  Windows          Intel Core i3   \n",
       "2         8           512          SSD  Windows          Intel Core i3   \n",
       "3         8           512          SSD  Windows  AMD Ryzen 5 Hexa Core   \n",
       "4         8           512          SSD  Windows          Intel Core i5   \n",
       "\n",
       "  Processor  \n",
       "0     Intel  \n",
       "1     Intel  \n",
       "2     Intel  \n",
       "3       AMD  \n",
       "4     Intel  "
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ae9f7a0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#EDA\n",
    "df_new = df[['Brand_name','Processor','RAM_Size',\"RAM_Type\",'Storage_size',\"Storage_type\",'OS_Type',\"MRP\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "c88d5d11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>Processor</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "      <th>MRP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>256</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>36990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>39990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>32990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP</td>\n",
       "      <td>AMD</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Brand_name Processor  RAM_Size RAM_Type  Storage_size Storage_type  OS_Type  \\\n",
       "0     Lenovo     Intel         8     DDR4           256          SSD  Windows   \n",
       "1     Lenovo     Intel         8     DDR4           512          SSD  Windows   \n",
       "2       ASUS     Intel         8     DDR4           512          SSD  Windows   \n",
       "3         HP       AMD         8     DDR4           512          SSD  Windows   \n",
       "4       ASUS     Intel         8     DDR4           512          SSD  Windows   \n",
       "\n",
       "       MRP  \n",
       "0  36990.0  \n",
       "1  39990.0  \n",
       "2  32990.0  \n",
       "3  49990.0  \n",
       "4  49990.0  "
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_new.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "4fa9c7b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 421 entries, 0 to 719\n",
      "Data columns (total 8 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   Brand_name    421 non-null    object \n",
      " 1   Processor     421 non-null    object \n",
      " 2   RAM_Size      421 non-null    int64  \n",
      " 3   RAM_Type      409 non-null    object \n",
      " 4   Storage_size  421 non-null    int64  \n",
      " 5   Storage_type  421 non-null    object \n",
      " 6   OS_Type       421 non-null    object \n",
      " 7   MRP           421 non-null    float64\n",
      "dtypes: float64(1), int64(2), object(5)\n",
      "memory usage: 29.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df_new.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "23a30c3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum : 14990.0\n",
      "Maximum : 434830.0\n",
      "Mean : 81363.63182897863\n",
      "Median : 61490.0\n",
      "Standard Deviation : 62584.16837149968\n"
     ]
    }
   ],
   "source": [
    "print(\"Minimum :\", df_new['MRP'].min())\n",
    "print(\"Maximum :\", df_new['MRP'].max())\n",
    "print(\"Mean :\", df_new['MRP'].mean())\n",
    "print(\"Median :\", df_new['MRP'].median())\n",
    "print(\"Standard Deviation :\", df_new['MRP'].std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "fd52d376",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Obervation : DEfinitely outliers present  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "3e3cc8f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x1afeebd2310>"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#MRP_analysis\n",
    "sns.displot(df_new['MRP'], rug= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "78ae1fe7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1224x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Outliers\n",
    "df_new['MRP'].plot(kind='box', figsize=(17,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "c5bbe430",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_new['MRP'].plot(kind='hist', figsize=(16,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "69106814",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='count', ylabel='RAM_Size'>"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#RAM_size analysis\n",
    "plt.figure(figsize = (16,5))\n",
    "sns.countplot( y = \"RAM_Size\" , data = df_new)\n",
    "\n",
    "\n",
    "#Obeservation : most popular one is the one with 8GB "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "72ae6dfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='RAM_Size', ylabel='MRP'>"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Price_vs_Ram_size\n",
    "plt.figure(figsize = (10,5))\n",
    "sns.boxplot(x='RAM_Size', y = 'MRP', data = df_new)\n",
    "\n",
    "#Obeservations: higher the proce for higher the RAM size , obviously"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "d7342a56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1aff197f550>"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure(figsize = (10, 6))\n",
    "plt.scatter(df_new.RAM_Size, df_new.MRP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "0a73fb56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Storage_size', ylabel='MRP'>"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA44AAAE+CAYAAADCok7IAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAprklEQVR4nO3df5xddX3n8dcnyQAJPxQyATFDje0ELf5CjYDrKiAkMOsvutXHou06dXFBVzO62nbBWkEUt9atrhNXd/2BDlZFlrYPonVKRgTdtggEwfCbGWuEKQiZBDAQfkySz/5xz+BNnDmTZH6ce++8no/HPO6c7z3n3M/95ubOfd/vOd8TmYkkSZIkSROZV3UBkiRJkqTGZnCUJEmSJJUyOEqSJEmSShkcJUmSJEmlDI6SJEmSpFIGR0mSJElSqQVVF9Ao2tvbc9myZVWXIUmSJEmVuPHGG0cyc8l49xkcC8uWLWP9+vVVlyFJkiRJlYiIX0x0n4eqSpIkSZJKGRwlSZIkSaUMjpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuDYREZGRli9ejWbN2+uuhRJkiRJc4jBsYn09fWxYcMG+vr6qi5FkiRJ0hxicGwSIyMj9Pf3k5n09/c76ihJkiRp1hgcm0RfXx+ZCcDOnTsddZQkSZI0awyOTWJgYIDR0VEARkdHWbduXcUVSZIkSZorDI5NYuXKlbS1tQHQ1tbGqlWrKq5IkiRJ0lxhcGwS3d3dRAQA8+bNo7u7u+KKJEmSJM0VBscm0d7eTldXFxFBV1cXixcvrrokSZIkSXPEgqoL0J7r7u5m48aNjjZKkiRJmlUGxybS3t7OmjVrqi5DkiRJ0hzjoaqSJEmSpFIGR0mSJElSKYOjJEmSJKmUwVGSJEmSVMrgKEmSJEkqZXCUJEmSJJUyOEqSJEmSShkcJUmSJEmlDI6SJEmSpFIGR0mSJElSKYOjJEmSJKnUjAfHiJgfETdFxHeL5cMiYiAiBovbQ+vWPS8ihiLirog4ra795RFxS3Ffb0RE0b5/RHy7aL8uIpbVbdNdPMZgRHTP9POUJEmSpFY1GyOO7wPuqFs+F7gqM5cDVxXLRMQxwJnAC4DTgc9HxPximy8AZwPLi5/Ti/azgIcysxP4DPDJYl+HAecDxwPHAefXB1RJkiRJ0p6b0eAYER3A64Av1zW/Cegrfu8DzqhrvzQzn8zMnwNDwHERcSRwSGZem5kJXLLbNmP7uhw4pRiNPA0YyMwtmfkQMMCvw6YkSZIkaS/M9Ijj/wT+FNhZ13ZEZt4PUNweXrQvBe6tW2+4aFta/L57+y7bZOZ24BFgccm+JEmSJEl7acaCY0S8HngwM2/c003GacuS9n3dpr7GsyNifUSs37Rp0x6WKUmSJElzy0yOOL4KeGNEbAQuBV4bEX8NPFAcfkpx+2Cx/jBwVN32HcB9RXvHOO27bBMRC4BnAFtK9rWLzPxiZq7IzBVLlizZ92cqSZIkSS1sxoJjZp6XmR2ZuYzapDc/yMw/BNYCY7OcdgNXFL+vBc4sZkp9LrVJcK4vDmfdGhEnFOcvvn23bcb29ebiMRK4ElgVEYcWk+KsKtokSZIkSXtpQQWP+RfAZRFxFnAP8BaAzLwtIi4Dbge2A+/JzB3FNu8GvgYsBPqLH4CvAF+PiCFqI41nFvvaEhEfA24o1rswM7fM9BOTJEmSpFYUtQE6rVixItevX191GZIkSZJUiYi4MTNXjHdfFSOO0pT19vYyNDQ0pX0MD9cm6+3o6JhkzXKdnZ309PRMaR+SJElSIzM4as56/PHHqy5BkiRJagoGRzWl6RjhG9tHb2/vlPclSZIktbKZvByHJEmSJKkFGBwlSZIkSaUMjpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuAoSZIkSSplcJQkSZIklTI4SpIkSZJKGRwlSZIkSaUMjpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuAoSZIkSSplcJQkSZIklTI4SpIkSZJKGRwlSZIkSaUWVF2A5qbe3l6GhoYqrWFwcBCAnp6eSuvo7OysvAZJkiSpjMFRlRgaGuLuW3/Cbx20o7Ia9hutDbg/sfGGymq459H5lT22JEmStKcMjqrMbx20gw+veLTqMir18fUHVV2CJEmSNCnPcZQkSZIklTI4SpIkSZJKeajqLJrqhDDDw8MAdHR0TKkOJ2ORJEmStDcMjk3k8ccfr7oESZIkSXOQwXEWTXWUb2z73t7e6ShHkiRJkvaI5zhKkiRJkkoZHCVJkiRJpQyOkiRJkqRSBkdJkiRJUimDoyRJkiSplMFRkiRJklTK4ChJkiRJKmVwlCRJkiSVMjhKkiRJkkoZHCVJkiRJpRZUXYDmpuHhYR7bOp+Prz+o6lIq9Yut8zlweLjqMiRJkqRSjjhKkiRJkko54qhKdHR08MT2+/nwikerLqVSH19/EAd0dFRdhiRJklTKEUdJkiRJUimDoyRJkiSplMFRkiRJklTK4ChJkiRJKmVwlCRJkiSVMjhKkiRJkkoZHCVJkiRJpQyOkiRJkqRSMxYcI+KAiLg+In4aEbdFxEeL9sMiYiAiBovbQ+u2OS8ihiLirog4ra795RFxS3Ffb0RE0b5/RHy7aL8uIpbVbdNdPMZgRHTP1POUJEmSpFY3kyOOTwKvzcyXAMcCp0fECcC5wFWZuRy4qlgmIo4BzgReAJwOfD4i5hf7+gJwNrC8+Dm9aD8LeCgzO4HPAJ8s9nUYcD5wPHAccH59QJUkSZIk7bkZC45Z82ix2Fb8JPAmoK9o7wPOKH5/E3BpZj6ZmT8HhoDjIuJI4JDMvDYzE7hkt23G9nU5cEoxGnkaMJCZWzLzIWCAX4dNSZIkSdJemNFzHCNifkTcDDxILchdBxyRmfcDFLeHF6svBe6t23y4aFta/L57+y7bZOZ24BFgccm+JEmSJEl7aUaDY2buyMxjgQ5qo4cvLFk9xttFSfu+bvPrB4w4OyLWR8T6TZs2lZQmSZIkSXPXrMyqmpkPA9dQO1z0geLwU4rbB4vVhoGj6jbrAO4r2jvGad9lm4hYADwD2FKyr93r+mJmrsjMFUuWLNn3JyhJkiRJLWwmZ1VdEhHPLH5fCJwK3AmsBcZmOe0Grih+XwucWcyU+lxqk+BcXxzOujUiTijOX3z7btuM7evNwA+K8yCvBFZFxKHFpDirijZJkiRJ0l5aMIP7PhLoK2ZGnQdclpnfjYhrgcsi4izgHuAtAJl5W0RcBtwObAfek5k7in29G/gasBDoL34AvgJ8PSKGqI00nlnsa0tEfAy4oVjvwszcMoPPVZIkSZJa1owFx8zcALx0nPbNwCkTbHMRcNE47euB3zg/MjOfoAie49x3MXDx3lUtSZIkSdrdrJzjKEmSJElqXgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuAoSZIkSSplcJQkSZIklTI4SpIkSZJKGRwlSZIkSaUMjpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuAoSZIkSSplcJQkSZIklVpQdQGau+55dD4fX39QZY//wLba9yZHLNpZWQ33PDqfoyt7dEmSJGnPGBxVic7OzqpL4KnBQQAOWLa8shqOpjH6QpIkSSpjcFQlenp6qi7h6Rp6e3srrkSSJElqbJ7jKEmSJEkqZXCUJEmSJJUyOEqSJEmSShkcJUmSJEmlDI6SJEmSpFIGR0mSJElSKYOjJEmSJKmUwVGSJEmSVMrgKEmSJEkqZXCUJEmSJJUyOEqSJEmSShkcJUmSJEmlDI6SJEmSpFJ7FBwjon2mC5EkSZIkNabS4BgRb4iITcAtETEcEf9mluqSJEmSJDWIyUYcLwJenZlHAr8P/PeZL0mSJEmS1EgWTHL/9sy8EyAzr4uIg2ehJmlSvb29DA0NTWkfg4ODAPT09ExpP52dnVPehyRJktTIJguOh0fEByZazsxPz0xZ0sxbuHBh1SVIkiRJTWGy4Pgl4OCSZakSjvBJkiRJs6c0OGbmRye6LyIOnP5yJEmS5o67776b973vfaxZs4bOzs6qy5GkCU16OY6IWBoRKyJiv2L58Ij4BDA449VJkiS1sAsuuIDHHnuMj3zkI1WXIkmlJrscx/uBm4E1wI8johu4A1gIvHymi5MkSWpVd999N8PDwwAMDw9PedI3SZpJk404ng08LzNfCZxB7RzH12Xmf83M+2e6OEmSpFZ1wQUX7LLsqKOkRjZZcHwiM7cAZOY9wN2Z+eOZL0uSJKm1jY02TrQsSY1ksllVOyKit2758PrlzHRqS0mSpH0QEWTmLsuS1KgmC45/stvyjTNViCRJ0lxy4okncs011zy9fNJJJ1VWiyRNZrLLcfTNViGSJElzSU9PDz/84Q/JTCLCaxRLamilwTEi1pbdn5lvnN5yJEmS5ob29vanRx1POukkFi9eXHVJkjShyQ5VfSVwL/At4DrAg+8lSZKmSU9PDw899JCjjZIa3mTB8VnASuCtwNuAvwe+lZm3zXRhkiRJra69vZ01a9ZUXYYkTar0chyZuSMz/yEzu4ETgCHgmohYPSvVSZIkSZIqN9mIIxGxP/A6aqOOy4Be4G9ntixJkiRJUqOYbHKcPuCFQD/w0cy8dVaqkiRJkiQ1jNJDVYH/CBwNvA/454j4VfGzNSJ+VbZhRBwVEVdHxB0RcVtEvK9oPywiBiJisLg9tG6b8yJiKCLuiojT6tpfHhG3FPf1RnGF3IjYPyK+XbRfFxHL6rbpLh5jMCK697pnJEmSZtjIyAirV69m8+bNVZciSaUmO8dxXmYeXPwcUvdzcGYeMsm+twMfzMzfpXZ+5Hsi4hjgXOCqzFwOXFUsU9x3JvAC4HTg8xExv9jXF4CzgeXFz+lF+1nAQ5nZCXwG+GSxr8OA84HjgeOA8+sDqiRJUiPo6+tjw4YN9PV56WxJjW2yEcd9lpn3Z+ZPit+3AncAS4E3AWPvjn3AGcXvbwIuzcwnM/Pn1CbiOS4ijgQOycxrMzOBS3bbZmxflwOnFKORpwEDmbklMx8CBvh12JQkSarcyMgI/f39ZCb9/f2OOkpqaDMWHOsVh5C+lNq1II/IzPuhFi6Bw4vVllK7ZuSY4aJtafH77u27bJOZ24FHgMUl+5IkSWoIfX191L4Th507dzrqKKmhzXhwjIiDgL8B3p+ZZedFxjhtWdK+r9vU13Z2RKyPiPWbNm0qKU2SJGl6DQwMMDo6CsDo6Cjr1q2ruCJJmtiMBseIaKMWGr+RmWOX8HigOPyU4vbBon0YOKpu8w7gvqK9Y5z2XbaJiAXAM4AtJfvaRWZ+MTNXZOaKJUuW7OvTlCRJ2msrV66kra0NgLa2NlatWlVxRZI0sUmv47ivinMNvwLckZmfrrtrLdAN/EVxe0Vd+zcj4tPAs6lNgnN9Zu4oZnE9gdqhrm8H1uy2r2uBNwM/yMyMiCuBT9RNiLMKOG8qz6e3t5ehoaGp7GLKBgcHAejp6am0DoDOzs6GqEOSpGbV3d1Nf38/APPmzaO720ngJTWuGQuOwKuoXc7jloi4uWj7ELXAeFlEnAXcA7wFIDNvi4jLgNupzcj6nszcUWz3buBrwEJq15TsL9q/Anw9IoaojTSeWexrS0R8DLihWO/CzNwylSczNDTETbfczs5Fh01lN1MST9WOtr3xZ7+srAaAedum1JWSJAlob2+nq6uLtWvX0tXVxeLFi6suSZImNGPBMTP/kfHPNQQ4ZYJtLgIuGqd9PfDCcdqfoAie49x3MXDxnta7J3YuOownjnn9dO6yKR1w+3erLkGSpJbQ3d3Nxo0bHW2U1PBmcsRRkiRJJdrb21mzZs3kK0pSxWblchySJEn6TSMjI6xevdprOEpqeAZHSZKkivT19bFhwwav4Sip4RkcJUmSKjAyMkJ/fz+ZSX9/v6OOkhqawVGSJKkCfX19ZNZmTN+5c6ejjpIamsFRkiSpAgMDA4yOjgIwOjrKunXrKq5IkiZmcJQkSarAypUraWtrA6CtrY1Vq1ZVXJEkTczgKEmSVIHu7m4iape8njdvntdylNTQDI6SJEkVaG9vp6uri4igq6uLxYsXV12SJE1oQdUFSJIkzVXd3d1s3LjR0UZJDc/gKEmSVJH29nbWrFlTdRmSNCkPVZUkSarIyMgIq1ev9hqOkhqewVGSJKkifX19bNiwwWs4Smp4BkdJkqQKjIyM0N/fT2bS39/vqKOkhmZwlCRJqkBfXx+ZCcDOnTsddZTU0AyOkiRJFRgYGGB0dBSA0dFR1q1bV3FFkjQxg6MkSVIFVq5cSVtbGwBtbW2sWrWq4ookaWIGR0mSpAp0d3cTEQDMmzfPazlKamgGR0mSpAq0t7fT1dVFRNDV1cXixYurLkmSJrSg6gIkSZLmqu7ubjZu3Ohoo6SGZ3CUJEmqSHt7O2vWrKm6DEmalIeqSpIkSZJKGRwlSZIkSaUMjpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkqSLf//73ec1rXsPVV19ddSmSVMrgKEmSVJFPfOITAHzsYx+ruBJJKmdwlCRJqsD3v/99tm/fDsD27dsddZTU0AyOkiRJFRgbbRzjqKOkRmZwlCRJqsDYaONEy5LUSAyOkiRJFViwYEHpsiQ1EoOjJKmljYyMsHr1ajZv3lx1KdIuPvShD+2y/Od//ucVVSJJkzM4SpJaWl9fHxs2bKCvr6/qUqRdnHrqqUQEABHBySefXHFFkjQxg6MkqWWNjIzQ399PZtLf3++ooxrKyMgI8+bVPorNmzfP16ekhmZwlCS1rL6+PjITgJ07dzrqqIbS19fHzp07AV+fkhqfZ2HvoeHhYeZte4QDbv9u1aVUbt62zQwPO/ObpMY3MDDA6OgoAKOjo6xbt44PfOADFVcl1axbt+7pLzYykyuvvNLXp6SG5YijJKllrVy5kra2NgDa2tpYtWpVxRU1Pycbmj7t7e2ly5LUSBxx3EMdHR088OQCnjjm9VWXUrkDbv8uHR3PqroMSZpUd3c3/f39QO0csu7u7ooran71kw05OjY19913X+myJDUSRxwlSS2rvb2drq4uIoKuri4WL15cdUlNzcmGJGnuMjhKklpad3c3L37xix1tnAZONjS9Tj311F2WV65cWVElkjQ5g6MkqaW1t7ezZs0aRxunwXiTDWnfnXPOObtcjuOcc86puCJJmpjnOEqSpD2ycuVK1q5dS2YSEXN+sqHe3l6GhoamtI8FCxbw1FNP8YxnPIOPfvSj+7SPzs5Oenp6plSHJE3GEUdJkrRH3vCGN+xy+Yg3vvGNFVfU/ObPn8+8efN49rOfXXUpklTKEUdJkrRHvvOd7xART484rl27dk7PrDodo3xj++jt7Z3yviRpJjniKEmS9sjAwMAuI46e4yhJc4fBUZIk7ZGVK1fS1tYGQFtb25w/x1GS5hKDoyRJ2iPd3d1EBFCbBdRLnEjS3GFwlCRJe6S9vZ2uri4igq6uLi9xIklziJPjSJKkPdbd3c3GjRsdbZSkOWbGRhwj4uKIeDAibq1rOywiBiJisLg9tO6+8yJiKCLuiojT6tpfHhG3FPf1RnGMTETsHxHfLtqvi4hlddt0F48xGBH+ZZMkSZKkKZjJQ1W/Bpy+W9u5wFWZuRy4qlgmIo4BzgReUGzz+YiYX2zzBeBsYHnxM7bPs4CHMrMT+AzwyWJfhwHnA8cDxwHn1wdUSZK07/r6+tiwYQN9fX1VlyJJmkUzFhwz80fAlt2a3wSM/aXpA86oa780M5/MzJ8DQ8BxEXEkcEhmXpu1+b8v2W2bsX1dDpxSjEaeBgxk5pbMfAgY4DcDrCRJ2ksjIyP09/eTmXzve99j8+bNVZckSZolsz05zhGZeT9AcXt40b4UuLduveGibWnx++7tu2yTmduBR4DFJfuSJElT0NfXx+joKACjo6OOOkrSHNIos6rGOG1Z0r6v2+z6oBFnR8T6iFi/adOmPSpUkqS5at26ddQOAILM5Morr6y4IknSbJnt4PhAcfgpxe2DRfswcFTdeh3AfUV7xzjtu2wTEQuAZ1A7NHaiff2GzPxiZq7IzBVLliyZwtOSJKn1HXHEEaXLkqTWNdvBcS0wNstpN3BFXfuZxUypz6U2Cc71xeGsWyPihOL8xbfvts3Yvt4M/KA4D/JKYFVEHFpMirOqaJMkSVPwwAMPlC5LklrXTF6O41vAtcDzImI4Is4C/gJYGRGDwMpimcy8DbgMuB34B+A9mbmj2NW7gS9TmzDnZ0B/0f4VYHFEDAEfoJihNTO3AB8Dbih+LizaJEnSFKxatWqX5dNOO22CNSVJrWbBTO04M986wV2nTLD+RcBF47SvB144TvsTwFsm2NfFwMV7XKwkSZrUq1/9aq644oqnl0888cQKq5EkzaYZC46taN62LRxw+3cre/x44lcA5AGHVFYD1PoBnlVpDZKk2fe5z31ul+XPfvazXHLJJRVVI0maTQbHPdTZ2Vl1CQwObgVg+e9UHdqe1RD9IUmaXRs3bixdliS1LoPjHurp6am6hKdr6O3trbgSSdJctGzZsl3C4rJlyyqrRZI0uwyOkujt7WVoaGhK+xgeHgago6NjkjUn1tnZ2RBf0kga34c//GHe+c53Pr38kY98pMJqJEmzyeAoaVo8/vjjVZcgSZKkGWJwlDQto3weSi21vo9//OO7LF944YVOjiNJc4TBUWpy03GY6XQYHBwEqj8f2MNdpZnj5DiSNHcZHKUmNzQ0xE233QTPrLiQnbWbm/71pupqeLi6h5bmglaaHMcv3Xbll26SJmNwlFrBM2HnSTurrqJy866ZV3UJmmaNMnET+MEaWmtynKGhIe669Q6OOrjaS1y1ba+9b237xUOV1XDv1l9W9tiSmofBUZLU0py4afocffTRT486Llu2rOmv6XvUwc/ig8e9o+oyKvdX13+16hIkNQGDo9TkhoeH4RFH2wB4GIZzuOoqNI2cuGl6TccI7sMPPwzAfvvtN6V/H0dwJam5+ElTkiTtsdHRUQ488EAWLVpUdSmSpFnkiKPU5Do6OtgUmzzHkdqoa8fSqZ3HJrUyR3AlSfvK4Ci1gocb4FDVR4vbgyqs4WFgaYWPL0mS1KIMjlKTa5TJKcamlF++dHl1RSxtnP6QJElqJQZHqck1yuQSHr6m8TTCtfIa5Tp54IQwkqTmZXCUNC0f7qfjw3kjfKju7e2lv79/SvvYtm0bmTlNFe27iJjyBCZdXV1T+jcZGhritlvu4JmLDp9SHVOx86kA4F9/trmyGgAe3vZgpY+vXQ0PD/PY1q1eioLadRwPHH6s6jIkNTiDo6RpsXDhwqpLUIN65qLDOfn5Z1ZdRuWuvvPSqkuQJGmfGRwlVT7K10h6enrsD2kO6OjoYNuOh/jgce+oupTK/dX1X2VRx6FVlyGpwXkdR0mSJElSKYOjJEmSJKmUwVGSJEmSVMpzHCVJagKNcGkTaJzLmzTCLMySNJcYHCVJagJDQ0Pc+tOfcvB+1f7p3r59BwC/uOO2ymrY+tT2yh5bkuYqg6MkSU3i4P0WcNwRzn55/QMPTct+7t36y8qv4/jgti0AHL7osMpquHfrL3kevq4klTM4SpKkOaezs7PqEgAYHRwBYNFzqgtuz+PQhukPSY3L4ChJkuacRjk/cqyO3t7eiiuRpHLOqipJkiRJKmVwlCRJkiSV8lBVSZKawPDwMFuf2j5tE8M0s61PbWd4eLjqMlSnt7eX/v7+fd5+27ZtZOY0VrTvIoJFixZNaR9dXV0Nczi0NF0ccZQkSZIklXLEUZKkJtDR0cGOrY94OQ5ql+Po6OiougzV6enpcYRtmkx19BZaawTX0dvG4YijJEmSJKmUI46SJElSg3D0dnq10ghu1effGhwlSWoSjTA5zrbtOwBYtGB+ZTVsfWp7ZY8tSXOVwVGSpCbQ2dlZdQkADA4OAvCc5csrraMR+qO3t5ehoaEp7WOsP6cywtTZ2ekIlTQBR3Cnj8FRkqQm0CgffMbq6O3trbiS1rBw4cKqS5CkPWJwlCTNmOHhYR7ZtpWr77y06lIq9/C2B8nhx6suQ9OoUcK8JM0GZ1WVJEmSJJVyxFGSNGM6OjqIJzdz8vPPrLqUyl1956Us7VhcdRmSJO0Tg6MkaUY9vO3BSg9VffSJ2iykBx1waGU1QK0flmJwlCQ1J4OjJGnGNMLMl4ODWwBY+jvVhralLK68PxplFlBwJlBJajYGR0nSjGmEYOAsoNPLWUAlaW4yOEqSGpYjZNOr2euXJFXH4DiLpvoByA8/krT3HCGTJGnqDI5NxA8/kuYav+SSJKkxGBxnkR+AJEmSJDWjeVUXIEmSJElqbAZHSZIkSVKplg6OEXF6RNwVEUMRcW7V9UiSJElSM2rZ4BgR84H/BXQBxwBvjYhjqq1KkiRJkppPywZH4DhgKDP/JTOfAi4F3lRxTZIkSZLUdFo5OC4F7q1bHi7aJEmSJEl7oZWDY4zTlrusEHF2RKyPiPWbNm2apbIkSZIkqbm0cnAcBo6qW+4A7qtfITO/mJkrMnPFkiVLZrU4SZIkSWoWrRwcbwCWR8RzI2I/4ExgbcU1SZIkSVLTWVB1ATMlM7dHxHuBK4H5wMWZeVvFZUmSJElS04nMnHytOSAiNgG/qLqOPdAOjFRdRAuxP6eX/Tl97MvpZX9OL/tzetmf08e+nF725/Rqhv58TmaOew6fwbHJRMT6zFxRdR2twv6cXvbn9LEvp5f9Ob3sz+llf04f+3J62Z/Tq9n7s5XPcZQkSZIkTQODoyRJkiSplMGx+Xyx6gJajP05vezP6WNfTi/7c3rZn9PL/pw+9uX0sj+nV1P3p+c4SpIkSZJKOeIoSZIkSSplcGwSEXFxRDwYEbdWXUsriIijIuLqiLgjIm6LiPdVXVMzi4hnRsTlEXFn0aevrLqmZhIRB0TE9RHx0+L1+NGi/VNFn26IiL+LiGdWXGrDGu89cqL+i4i2iOiLiFuK1+t5lRXegCZ6f4yICyLiXyPi5uLn39Vt8+KIuLZY/5aIOKC6Z9B4ImJj0S83R8T6ou0tRX/tjIgVdeuujIgbi/VvjIjXVld5NUpeg4dFxEBEDBa3hxbti4v1H42Iz+22r/9QvAfcFhF/Wdf+moj4SURsj4g3z+4znF2z1J8fiIjbi/uuiojnzO6znB370JcT/n+OiIsi4t6IeHS3x2jY16bBsXl8DTi96iJayHbgg5n5u8AJwHsi4piKa2pmnwX+ITOfD7wEuKPieprNk8BrM/MlwLHA6RFxAjAAvDAzXwzcDRhwJvY1fvM9cqL+ewuwf2a+CHg5cE5ELJulOptB2fvjZzLz2OLnewARsQD4a+BdmfkC4CRgtIK6G93JRb+NhcRbgX8P/Gi39UaANxSvz27g67NYY6OY6DV4LnBVZi4HriqWAZ4A/hz44/qdRMRi4FPAKcVr84iIOKW4+x7gj4BvzvBzaQSz0Z83ASuK99vLgb+kNe1tX5b9f/4OcNw4j9Gwr02DY5PIzB8BW6quo1Vk5v2Z+ZPi963Ugs7SaqtqThFxCPAa4CsAmflUZj5caVFNJmvGvnFsK34yM9dl5vai/cdARyUFNoHx3iNL+i+BA4vAsxB4CvjVbNXa6Pbh/XEVsCEzf1psszkzd8x8pc0tM+/IzLvGab8pM+8rFm8DDoiI/We3umqVvAbfBPQVq/UBZxTrPJaZ/0gt8NT7beDuzNxULH8f+P1im42ZuQHYOYNPpSHMUn9enZnbivaW/Xu1D3054f/nzPxxZt4/zmM07GvT4Kg5rxhpeClwXcWlNKvfBjYBX42ImyLiyxFxYNVFNZuImB8RNwMPAgOZufvr8T8B/bNeWOuo77/LgceA+6l9s/s/MtMv5sYxzvvje4tD0S4eOxQLOBrIiLiyOLzqT6uotcElsK44VO3svdju94GbMvPJGaqr4e32Gjxi7IN2cXv4JJsPAc+PiGXFF0VnAEfNXLWNb5b68yzmwN+rfejLpv//bHDUnBYRBwF/A7w/Mx1x2DcLgJcBX8jMl1L7QH5u+SbaXWbuyMxjqX1Le1xEvHDsvoj4M2qHx3yjovKa2jj9dxywA3g28FzggxHx2xWV17DGeX/8AvA71A6nvh/4q2LVBcC/Bf6guP29usPXVPOqzHwZ0EXt0LbXTLZBRLwA+CRwzkwX16im+jc6Mx8C3g18G/h/wEZq7wVz0mz0Z0T8IbCC2iGtLWtv+7JV/j8bHDVnRUQbtf/038jMv626niY2DAzXjZBdTi1Iah8Uh/leQ3G+XkR0A68H/iC9ftJem6D/3kbtnNzRzHwQ+CdqH3RUGO/9MTMfKL7g2Al8iV+fmzMM/DAzR4pD1b6H7wG7GDtUrXi9/R3jn9f0tIjoKNZ7e2b+bOYrbDwT/I1+ICKOLO4/ktoRGqUy8zuZeXxmvhK4CxicqZob2Wz0Z0ScCvwZ8MZmHlWbzN72ZSv9fzY4ak6KiKB2Tt4dmfnpqutpZpn5S+DeiHhe0XQKcHuFJTWdiFgSv57xcyFwKnBnRJwO/Ddqf4S3lexC4yjpv3uA10bNgdQmOLizihob0UTvj2Mfigq/R21yF4ArgRdHxKLi8LUT8T3gaRFxYEQcPPY7tXNCJ5whvXgv+HvgvMz8p1kpssGU/I1eS22CEYrbK/ZgX4cXt4cC/wX48vRW2/hmoz8j4qXA/6H2fjtpAG1We9uXrfb/OfwCuzlExLeozVTXDjwAnJ+ZX6m0qCYWEf+W2mEWt/Drk48/lMUsgdo7EXEstT8e+wH/AryjOKRFeyAiXkztZPr51L7QuywzL4yIIWB/YHOx6o8z810VldnQxnuPpDaL6m/0X3GI0VeBY4AAvpqZLX1Y1d6Y6P0ReCu1w1ST2iFq54yd01McnnZecd/3MtPzHAvFYdB/VywuAL6ZmRdFxO8Ba4AlwMPAzZl5WkR8mFpf1o+MrWrlD+O7K3kNXgdcBvwWtS+A3jJ2fnJEbAQOofZ36GFqfXZ78d7wkmIfF2bmpcX6r6D273IotUlgfpm1mUJbziz15/eBF1E7jB3gnsx848w+s9m3t31Z9v85apczeRu10ybuA76cmRc08mvT4ChJkiRJKuWhqpIkSZKkUgZHSZIkSVIpg6MkSZIkqZTBUZIkSZJUyuAoSZIkSSplcJQkSZIklTI4SpK0m4j4s4i4LSI2RMTNEXF8RLw/IhZVXdueiIjvFReeliRpWngdR0mS6kTEK4FPAydl5pMR0U7tItj/DKzIzJG92Nf8zNwxQ6VKkjRrHHGUJGlXRwIjmfkkQBEU3ww8G7g6Iq4GiIi3RsQtEXFrRHxybOOIeDQiLoyI64BXRsRHIuKGYr0vRkQU672iGNG8NiI+FRG3Fu3zi+UbivvPmajQiDgyIn5UjIreGhGvLto3RkR7RLyruO/miPh5Xe2risf9SUT834g4aEZ6UpLUMgyOkiTtah1wVETcHRGfj4gTM7MXuA84OTNPjohnA58EXgscC7wiIs4otj8QuDUzj8/MfwQ+l5mvyMwXAguB1xfrfRV4V2a+EqgflTwLeCQzXwG8AvjPEfHcCWp9G3BlZh4LvAS4uf7OzPzfxX2vAIaBTxcjqB8GTs3MlwHrgQ/sdS9JkuYUg6MkSXUy81Hg5cDZwCbg2xHxR7ut9grgmszclJnbgW8Arynu2wH8Td26J0fEdRFxC7Wg+YLi/MODM/Ofi3W+Wbf+KuDtEXEzcB2wGFg+Qbk3AO+IiAuAF2Xm1gnW+yzwg8z8DnACcAzwT8VjdAPPmWA7SZIAWFB1AZIkNZrivMRrgGuKwNe92ypRsvkTY+c1RsQBwOepnRt5bxHwDphk+wBWZ+aVe1DnjyLiNcDrgK9HxKcy85JddlYLvc8B3lu3/4HMfOtk+5ckaYwjjpIk1YmI50VE/QjfscAvgK3AwUXbdcCJxXmE84G3Aj8cZ3cHFLcjxXmEbwbIzIeArRFxQnH/mXXbXAm8OyLainqOjogDJ6j1OcCDmfkl4CvAy3a7/+XAHwN/mJk7i+YfA6+KiM5inUURcfSEHSJJEo44SpK0u4OANcXhpNuBIWqHrb4V6I+I+4vzHM8DrqY2gve9zLxi9x1l5sMR8SXgFmAjtUNLx5wFfCkiHqM2uvlI0f5lYBnwk2IinU3AGRPUehLwJxExCjwKvH23+98LHEZtUh+A9Zn5zmIU8lsRsX+x3oeBu8s6RZI0t3k5DkmSKhARBxXnUxIR5wJHZub7Ki5LkqRxOeIoSVI1XleMWi6gdijsH1VbjiRJE3PEUZKkBhcRLwK+vlvzk5l5fBX1SJLmHoOjJEmSJKmUs6pKkiRJkkoZHCVJkiRJpQyOkiRJkqRSBkdJkiRJUimDoyRJkiSp1P8HrCur+azK/KEAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Storage_size_vs_Price\n",
    "plt.figure(figsize=(15, 5))\n",
    "sns.boxplot(x='Storage_size', y ='MRP', data=df_new)\n",
    "\n",
    "#OBservation: Again more the storage most the price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "e4fcbe9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAArsAAAJDCAYAAAALotz2AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAz40lEQVR4nO3debxd89n38c91zkGQxJgEMVTNs5q1aqjSUBUeamqLFuEu2t7qrqI1Vatoe7daLakq8YjQEsITQ2umaLRUilI1JKEyIBGJKXE9f+yddOfk5Axy9tln7/V5e51Xztrrt9f+rTjDle++1m9FZiJJkiQ1oqZaT0CSJEmqFotdSZIkNSyLXUmSJDUsi11JkiQ1LItdSZIkNSyLXUmSJDUsi11JkiTVXERcHhFTIuLvi9gfEXFRRDwXEU9ExFadOa7FriRJknqDK4Ah7ezfC1iv/DEM+FVnDmqxK0mSpJrLzPuA19sZMhQYkSUPA8tHxKodHbeluybYnthjdW/TpsJ769anaz0FqaZ2ufLIWk9BqqlHj7o+aj2H1nq0Rvvjy8dSSmTnGZ6Zw7twhMHAxIrtSeXH/t3ek3qk2JUkSVKxlQvbrhS3rbX1j4UOi3WLXUmSpKKKXhc2t2cSsEbF9urAKx09yZ5dSZIk1YMxwOHlVRl2AGZkZrstDGCyK0mSpF4gIq4BdgVWjohJwJnAEgCZeQkwFtgbeA6YDXy5M8e12JUkSSqqXvQef2Ye2sH+BI7v6nF70SlKkiRJ3ctkV5Ikqajq6wK1D8VkV5IkSQ3LZFeSJKmoGj/YNdmVJElS4zLZlSRJKip7diVJkqT6ZbIrSZJUVAWIPQtwipIkSSoqk11JkqSismdXkiRJql8mu5IkSUXV+MGuya4kSZIal8muJElSUTU1frRrsitJkqSGZbErSZKkhmUbgyRJUlE1fheDya4kSZIal8muJElSUXlTCUmSJKl+mexKkiQVVeMHuya7kiRJalwmu5IkSUXlTSUkSZKk+mWyK0mSVFSNH+ya7EqSJKlxmexKkiQVlevsSpIkSfXLZFeSJKmoXI1BkiRJql8mu5IkSUXV+MGuya4kSZIal8WuJEmSGpZtDJIkSUXl0mOSJElS/TLZlSRJKqrGD3ZNdiVJktS4THYlSZKKyptKSJIkSfXLZFeSJKmoGj/YNdmVJElS4zLZlSRJKirX2ZUkSZLql8muJElSURUg9izAKUqSJKmoTHYlSZKKyp5dSZIkqX6Z7EqSJBVV4we7JruSJElqXBa7kiRJali2MUiSJBWVF6hJkiRJ9ctkV5IkqagKEHsW4BQlSZJUVCa7kiRJRWXPriRJklS/THYlSZKKqvGDXZNdSZIkNS6TXUmSpKJqavxo12RXkiRJDctkV5IkqahcjUGSJEmqXya7kiRJRdX4wa7JriRJkhpXp4vdiBgUEb+JiFvL2xtHxFHVm5okSZKqKSJ67KNWupLsXgHcDqxW3n4W+EY3z0eSJEnqNl0pdlfOzOuADwAycw4wtyqzkiRJUtWZ7C5oVkSsBCRAROwAzKjKrCRJkqRu0JXVGL4JjAHWiYgHgQHA56syK0mSJKkbdLrYzcy/RMQuwAaUFqp4JjPfr9rMJEmSVFUFuKdEl1Zj+BdwdGY+mZl/z8z3I+KWKs5NkiRJWixdaWN4H9gtIrYHjs3M94DB1ZmWJEmSqq2pANFuVy5Qm52ZBwNPA/dHxFqUL1aTJEmSeqOuJLsBkJkXRMRfKK25u2JVZiVJkqSqq+WSYD2lK8XuGfM+ycw7I+IzwBHdPyVJkiSpe3RY7EbEhpn5D+DliNiq1W4vUJMkSapTJrslJwHDgB+3sS+BT3XrjCRJkqRu0mGxm5nDyn/uVv3pSJIkqacUIdntcDWGiNg2Ilap2D48Im6KiIsiwgvUJEmS1Gt1ZumxS4H3ACJiZ+CHwAhgBjC8elOTJElSNUX03EetdKZntzkzXy9/fjAwPDOvB66PiMerNjNJkiRpMXWq2I2IlsycA+xO6WK1rjxfNfSbb/6Ifbb/NFOmT2OzYZ+u9XSkbpOZXHjej3jgvgfps3Qfzv7+WWy08YYLjXt50sucevJpzJjxJhtuvCHnnncOSyy5BDNnvsV3Tvkur/77VebOncuXvvxFhu6/LwAjr7qG0b8fTSbsf+B+fOHww3r69KQu2XHwlpy8w1doamrixmfu5MonRi80ZutVNuGkHb5MS1ML0995k2PHllYUHXPQr5j9/tvMzQ+Y+8FcDh9zSk9PXzVUhJ7dzhSr1wD3RsQ04G3gfoCIWJdSK4N6sSvu+B2/uOkKRnzrp7WeitStHrz/QSa8NJGbbh3N+Cf+znnnnMeIUVcuNO6in/ycLxx+GJ/Z+zN8/+wfcOMNN/H5Qw7kumuu46PrrM3Pfvm/vPH6G+z/2QPY+7N78dJLLzH696MZMWoESyzRwgnHfo1P7rITa661Zg3OUupYUzRxyseP4fjbzmHyrNcYse/53DdhHC9MnzR/TN8ll+GUjx/Dibefy+RZ01ihT/8FjnHs2DOZ8e7Mnp661CM67NnNzO8D3wSuAHbKzHm3CG4CTpw3LiJWqMYEtXjuH/8Ir8+cXutpSN3unrvuZZ999yYi2HyLzZg5cyZTp05bYExmMu6Rcey+5+4A7DN0H+6+8x6glGbMnjWbzGT27Nn0X64/zS3NvPD8i2y2xWYsvXQfWlpa2Hqbrbjrj3f39OlJnbbJgHWZ+OarvDxzMnM+mMMdzz/ALmtuu8CYIet8krtfeoTJs0rfI2+882YtpqpeKCJ67KNWOnOBGpn5cGaOzsxZFY89m5l/rRh2Z7fPTpIWYcqUqQxaZf5CMQwcNIipk6csMGb69Bn07dePlpbSm1iDBg1k6pTSmIMPO4gXnn+Bz+w6hIP2O4T/OfVkmpqaWGfddfjro48xffp03n77HR64/0Emvzq5505M6qKBy6w4v4gFmDL7dQYuu9ICY9bsvxr9llyWS/c+m6uGXsBn191l/r4kuXjIGVw19AL232CPHpu31FO6s+d2gZI9IoYxr793w+Vh9WW78aUkFd78N5kqtE4O2hgzL1146IGHWH/D9bn0t5cwccIkvnrM8Xxs6y356Dprc+RRh/PVo49n6WWWYf0N1qO5ubkaZyB1k4UTs2z1td/S1MxGK6/Df916Fks1L8lvP3ce46c8y4Q3/81Rt5zOtNlvsEKf/lw85ExenPEyj736VE9NXqq6TiW7nbTAd1ZmDs/MbTJzGwtdSd3h2pHXccj/OYxD/s9hDBgwgMmvvjp/35TJkxkwcMAC45dfYXnemjmTOXPmADB58hRWHlAaM+bGm/nUHp8iIlhzrTVYbfBqvPj8iwDsd8B+jPz91fxmxK/pv9xy9uuqV5sy+zUGLbvy/O2By6zI1NmvLzBm8qzXeGjSY7wz511mvDuTx159ivVW/AgA02a/AZRaG+556RE2WXndHpu7ai968L9a6c5iV5Kq6uDDDmLUDSMZdcNIdt19V24ZM5bM5Im/jadv374MGLDyAuMjgm2224Y77yh1Wd1y0y3s+qnS27errLoKf374zwC8Nu01XnrxJQavsToAr79WKhT+/cqr3P3Huxiy92d66hSlLntq6nOs0X9VVus7kJamFvb86E7cN+HRBcbc+9Kf2XKVjWiOJpZqXpJNB67HizMm0adlKZZZog8AfVqWYvvBW/CvNybU4jSkqqlaG4N6h5Gn/YJdN9+RlZdbkYkjx3HmiB9z+W2jaj0tabHttPMneOC+Bxm613706dOHs849c/6+E4/7Gmec810GDBzA1046kVNPPo2LL/oVG260AfsdMBSAY447mjNPP4uD9juYzORrJ53ICissD8DJ3/gWM6bPoKWlhVO+cwr9l+vf1hSkXmFufsCFD13Gz4d8l+ZoYsyzd/H89IkcsOGeAFz/jzt4ccbLPDTpca7Z/yckyY3P/JF/vTGRwf0GceHu3wKguamZ2/91Pw+9/HgNz0Y9rQhLj0Xrvp6FBnRwS+B5N5yIiBUrbj6x4DH2WL39F5EK4K1bn671FKSa2uXKI2s9BammHj3q+l5XWfY/dfseq9HePO+RDs8/IoYAPwOagcsy84et9i8H/F9gTUqh7Y8y87ftHbMzye40YBIwZ97rVOxL4KPwn6JXkiRJ9aE3BbsR0QxcDOxBqfYcFxFjMrPyisnjgacy83MRMQB4JiKuzsz3FnXczhS7Pwd2BR6kdIOJB7KjOFiSJEnqmu2A5zLzeYCIGAUMBSqL3QT6Ran/oi/wOv8JZNvUYbGbmV8vH3BX4EvAzyPiDuBXmfnChzgRSZIk9QJNPRjtLrAsbcnwzBxesT0YmFixPQnYvtVhfgGMAV4B+gEHZ+YH7b1upy5QKye5d0fEY8AhwPeAfwK/7szzJUmSVGzlwnZ4O0PaqrxbdxN8Bngc+BSwDvCHiLg/Mxd5W8AOi92IWJZShHwwMAC4AdgqMye2+0RJkiT1ar1sNYZJwBoV26tTSnArfRn4YTmIfS4iXgA2BP68qIN2JtmdQinFvQZ4jlKFvW1EbAuQmTd09gwkSZKkRRgHrBcRawMvU+omOKzVmAnA7sD9ETEI2AB4vr2DdqbY/R2lAnfD8kelpJT0SpIkqc70pmQ3M+dExAnA7ZSWHrs8M5+MiOPK+y+h1Ep7RUSMp9T2cEpmTmvvuJ25QO3IRe0rV9SSJEnSYsvMscDYVo9dUvH5K8CeXTlml++gVl7M9wBKsfJGlK6ckyRJUp3pRcFu1XSq2I2IpYF9KRW4W1Fa6mE/4L6qzUySJElaTJ1ZjeFqYGfgDkprm91FacHfe6o7NUmSJFVTb+rZrZamTozZFHgDeBr4R2bOZeE1zyRJkqRep8NiNzO3AA4C+gN/jIj7Kd2mbZVqT06SJElaHJ29g9o/gDOAMyJiG0q9u3+OiEmZ+fFqTlCSJEnVYRtDGzLz0cw8CVgX+GX3T0mSJEnqHh0WuxHRPyJOjYhfRMSeUXIC8Czw+epPUZIkSdUQET32USudaWO4itIFag8BRwP/AywJ7JeZj1dvapIkSdLi6Uyx+9HM3AwgIi4DpgFrZubMqs5MkiRJVWXPbsn78z4pLzv2goWuJEmS6kFnkt0tIuLN8ucBLF3eDiAzs3/VZidJkqSqKUCw23Gxm5nNPTERSZIkqbt1ap1dSZIkNR57diVJkqQ6ZrIrSZJUUCa7kiRJUh0z2ZUkSSqoJpNdSZIkqX6Z7EqSJBVUAYJdk11JkiQ1LotdSZIkNSzbGCRJkgrKpcckSZKkOmayK0mSVFCBya4kSZJUt0x2JUmSCsqeXUmSJKmOmexKkiQVlMmuJEmSVMdMdiVJkgqqAMGuya4kSZIal8muJElSQdmzK0mSJNUxk11JkqSCMtmVJEmS6pjJriRJUkGZ7EqSJEl1zGJXkiRJDcs2BkmSpIIqQBeDya4kSZIal8muJElSQXmBmiRJklTHTHYlSZIKymRXkiRJqmMmu5IkSQVlsitJkiTVMZNdSZKkgipAsGuyK0mSpMZlsitJklRQ9uxKkiRJdcxkV5IkqaBMdiVJkqQ6ZrIrSZJUUCa7kiRJUh2z2JUkSVLDso1BkiSpoArQxWCyK0mSpMZlsitJklRQXqAmSZIk1TGTXUmSpKIy2ZUkSZLql8muJElSQdmzK0mSJNUxk11JkqSCKkCwa7IrSZKkxmWyK0mSVFD27EqSJEl1zGRXkiSpoEx2JUmSpDpmsitJklRQJruSJElSHbPYlSRJUsOyjUGSJKmgCtDFYLIrSZKkxmWyK0mSVFBeoCZJkiTVsR5Jdt+69emeeBmpV+u710a1noJUU2/f9mytpyCpFZNdSZIkqY7ZsytJklRQJruSJElSHTPZlSRJKiiTXUmSJKmOmexKkiQVVAGCXZNdSZIkNS6TXUmSpIKyZ1eSJEmqYya7kiRJBWWyK0mSJPWQiBgSEc9ExHMR8e1FjNk1Ih6PiCcj4t6OjmmyK0mSpJqLiGbgYmAPYBIwLiLGZOZTFWOWB34JDMnMCRExsKPjWuxKkiQVVC9rY9gOeC4znweIiFHAUOCpijGHATdk5gSAzJzS0UFtY5AkSVJvMBiYWLE9qfxYpfWBFSLinoj4S0Qc3tFBTXYlSZIKqieD3YgYBgyreGh4Zg6vHNLG07LVdguwNbA7sDTwUEQ8nJnPLup1LXYlSZJUdeXCdng7QyYBa1Rsrw680saYaZk5C5gVEfcBWwCLLHZtY5AkSSqoiOixj04YB6wXEWtHxJLAIcCYVmNuAj4ZES0RsQywPfB0ewc12ZUkSVLNZeaciDgBuB1oBi7PzCcj4rjy/ksy8+mIuA14AvgAuCwz/97ecS12JUmSiqp3rcZAZo4FxrZ67JJW2xcCF3b2mLYxSJIkqWGZ7EqSJBVUL1tntypMdiVJktSwTHYlSZIKqqnxg12TXUmSJDUuk11JkqSCsmdXkiRJqmMmu5IkSQXVZLIrSZIk1S+LXUmSJDUs2xgkSZIKygvUJEmSpDpmsitJklRQRUg9i3COkiRJKiiTXUmSpIJy6TFJkiSpjpnsSpIkFZSrMUiSJEl1zGRXkiSpoOzZlSRJkuqYya4kSVJB2bMrSZIk1TGTXUmSpIIqQupZhHOUJElSQZnsSpIkFZSrMUiSJEl1zGJXkiRJDcs2BkmSpIJy6TFJkiSpjpnsSpIkFZQXqEmSJEl1zGRXkiSpoBo/1zXZlSRJUgMz2ZUkSSooe3YlSZKkOmayK0mSVFAmu5IkSVIdM9mVJEkqKO+gJkmSJNUxk11JkqSCsmdXkiRJqmMmu5IkSQXV+Lmuya4kSZIaWKeT3YhYBvgmsGZmHhMR6wEbZOYtVZudJEmSqsae3QX9FngX2LG8PQk4t9tnJEmSJHWTrhS762TmBcD7AJn5NsVo9ZAkSVKd6soFau9FxNJAAkTEOpSSXkmSJNWhIrQxdKXYPQu4DVgjIq4GPgEcWYU5SZIkSd2i08VuZt4REX8BdqDUvvD1zJxWtZlJkiSpqrxdcIWIuBPYPjP/X2bekpnTImJ4FecmSZIkLZautDGsDZwSEdtm5tnlx7apwpwkSZLUA4rQs9uV1RimA7sDgyLi5ohYrjpTkiRJkrpHV5LdyMw5wFcj4kjgAWCFqsxKkiRJVdf4uW7Xit1L5n2SmVdExHjg+O6fkiRJktQ9Oix2I6J/Zr4J/C4iVqzY9QJwctVmJkmSpKoqQs9uZ5LdkcA+wF8o3VCi8m8lgY9WYV6SJEnSYuuw2M3Mfcp/rl396UiSJKmnFCHZ7co6u5+IiGXLn38xIn4SEWtWb2qSJEnS4unK0mO/AmZHxBbAt4CXgKuqMitJkiRVXUT02EetdKXYnZOZCQwFfpaZPwP6VWdakiRJ0uLrytJjMyPiVOCLwM4R0QwsUZ1pSZIkqdq6knrWq66c48HAu8BRmfkqMBi4sCqzkiRJkrpBp5PdcoH7k4rtCcCIedsR8VBm7ti905MkSZI+vK60MXSkTzceS5IkSVVWywvHekp3tmpkNx5LkiRJWmzdmexKkiSpjnhTia5p/L8tSZIk1ZUuFbsRsVZEfLr8+dIRUbnO7pe6dWZapMzkgh9cyL5D9uOg/Q/h6af+0ea4lye9zOGHHMHQvfbnlG+eyvvvvQ/AzJlv8fWv/jcH738oB+57EDeNHjP/OSOvuobPDz2IA/c9iKtHjOyR85Gq6Tff/BGTr3uc8cP/WOupSFWTmfzw++ezz2f25cD9DuLpp55uc9w1V49in8/syxYbf4w33nhj/uMvPP8CXzr0cLbZYjuuvHxEm89VY2qK6LGPmp1jZwdGxDHA74FLyw+tDtw4b39m/r1bZ6ZFevD+B5nw0kRuunU03znrdM4757w2x130k5/zhcMP46ZbR9O/fz9uvOEmAK675jo+us7aXDv6Gn59xaX87wU/5f333ue5fz7H6N+PZsSoEYy6YST33/sAE16a0JOnJnW7K+74HUNO+2KtpyFV1QP3lX5e33zbTZxx9nc49+wftDluy49tyaWXX8Jqq626wOP9l1uOU047hSO+fHhPTFfqUV1Jdo8HPgG8CZCZ/wQGVmNSat89d93LPvvuTUSw+RabMXPmTKZOnbbAmMxk3CPj2H3P3QHYZ+g+3H3nPUDpysvZs2aTmcyePZv+y/WnuaWZF55/kc222Iyll+5DS0sLW2+zFXf98e6ePj2pW90//hFenzm91tOQquruu+7lc0P3Kf9e2Lz8e2HqQuM22nhDBg9ebaHHV1ppRTbdbBNaWryUp2i8XfCC3s3M9+ZtREQLrsBQE1OmTGXQKqvM3x44aBBTJ09ZYMz06TPo26/f/B9cgwYNZOqU0piDDzuIF55/gc/sOoSD9juE/zn1ZJqamlhn3XX466OPMX36dN5++x0euP9BJr86uedOTJL0oUyZMmWB3wuDBg1iSqvfC1JRdeWfcPdGxGnA0hGxB/BV4OZFDY6IYcAwgIt++TO+csyXF2uiqpBt/Buj9b+Y2hgz719VDz3wEOtvuD6X/vYSJk6YxFePOZ6Pbb0lH11nbY486nC+evTxLL3MMqy/wXo0NzdX4wwkSd2pnZ/5UnuaCrC+QFeK3W8DRwHjgWOBscBlixqcmcOB4QCz5sw0AV5M1468jtG/vxGATTbdmMmvvjp/35TJkxkwcMAC45dfYXnemjmTOXPm0NLSwuTJU1h5QGnMmBtv5sijjyQiWHOtNVht8Gq8+PyLbLr5pux3wH7sd8B+APz8pxczaJCdKpLUG40aeS03/O4GADbZbJMFfi9MbuP3glRUnW5jyMwPMvPXmfn5zDyw/LlFbA85+LCDGHXDSEbdMJJdd9+VW8aMJTN54m/j6du3LwMGrLzA+Ihgm+224c477gTglptuYddP7QLAKquuwp8f/jMAr017jZdefInBa6wOwOuvvQ7Av195lbv/eBdD9v5MT52iJKkLDjnsYK4bfS3Xjb6W3XbfjZtvuqX8e+EJ+vbry4ABFrvqWBF6dqOz9WpEjGfhHt0ZwKPAuZn52qKea7LbvTKTH557AQ89+Cf69OnDWeeeycabbgzAicd9jTPO+S4DBg5g0sRJnHryacyY8SYbbrQB557/PZZcckmmTpnKmaefxbSp08hMjjz6SD77ub0B+MqXjmbG9Bm0tLRw0in/zfY7bFfLU20offfaqNZTKKSRp/2CXTffkZWXW5HJb0zjzBE/5vLbRtV6WoX09m3P1noKDSszOe/cH/LgA6XfC+d8/yw22XQTAI4/9gTO/N4ZDBw4kKuvGskVl1/Ja9NeY8UVV2CnnXfirO+dybSp0zj0oC8w661ZNDUFSy+zDKNvvp6+ffvW+MwaS5/mZXpdz8Apfzq1x2q08z9+Xk3OvyvF7gXAXGDe4quHlP98E9gpMz+3qOda7EoWu5LFroquNxa7pz50Wo/VaOft+IOanH9XenY/kZmfqNgeHxEPZuYnIsJFLCVJktTrdGXpsb4Rsf28jYjYDpj3/sacbp2VJEmSqi568L9a6UqyezRweUT0BYJS+8LREbEs0PYtvCRJkqQa6nSxm5njgM0iYjlKvb7TK3Zf190TkyRJkhZXl+4LGBGfBTYB+sxbQiIzz6nCvCRJklRlRbj5SKd7diPiEuBg4ERKbQyfB9aq0rwkSZKkxdaVZPfjmbl5RDyRmWdHxI+BG6o1MUmSJFVXk8nuAt4p/zk7IlYD3gfW7v4pSZIkSd2jK8nuzRGxPHAh8FdKd1P7dTUmJUmSpOqLLuWe9alTxW5ENAF3lldguD4ibgH6ZOaMak5OkiRJWhydKnYz84Nyj+6O5e13gXerOTFJkiRVlz27C7ojIg6IIqxRIUmSpIbQlZ7dk4BlgbkR8Tal5ccyM/tXZWaSJEmqqiJkmJ1OdjOzX2Y2ZeYSmdm/vG2hK0mSpG4REUMi4pmIeC4ivt3OuG0jYm5EHNjRMbt6B7V9gZ3Lm/dk5i1deb4kSZJ6j6D3JLsR0QxcDOwBTALGRcSYzHyqjXHnA7d35rhduYPaD4GvA0+VP75efkySJElaXNsBz2Xm85n5HjAKGNrGuBOB64EpnTloV5LdvYEtM/MDgIi4EngMWGTELEmSpN6rJ1djiIhhwLCKh4Zn5vCK7cHAxIrtScD2rY4xGNgf+BSwbWdet0ttDMDywOvlz5fr4nMlSZJUUOXCdng7Q9qqvLPV9k+BUzJzbmcvrutKsXse8FhE3F2ezM7AaV14viRJknqRXrYawyRgjYrt1YFXWo3ZBhhVnvfKwN4RMSczb1zUQTtd7GbmNRFxD6XIOChV1a929vmSJElSO8YB60XE2sDLwCHAYZUDMnPteZ9HxBXALe0VutCFYjci7szM3YExbTwmSZIkfWiZOSciTqC0ykIzcHlmPhkRx5X3X/JhjtthsRsRfYBlgJUjYgX+00/RH1jtw7yoJEmSaq+pSzfTrb7MHAuMbfVYm0VuZh7ZmWN2Jtk9FvgGpcL2LxWPz6S0FpokSZLUK3Wm2P0TcB1wYGb+PCKOAA4AXgRGVnFukiRJqqJedoFaVXQmu74UeLdc6O5MaVWGK4EZtL98hCRJklRTnUl2mzNz3tq6B1NaAPh64PqIeLxqM5MkSVJVmeyWNEfEvKJ4d+Cuin1dvSmFJEmS1GM6U6xeA9wbEdOAt4H7ASJiXUqtDJIkSapDTW3etKyxdFjsZub3I+JOYFXgjsycd9u2JuDEak5OkiRJWhydakPIzIfbeOzZ7p+OJEmSeoo9u5IkSVId8wIzSZKkgmoy2ZUkSZLql8muJElSQUUBVmMw2ZUkSVLDMtmVJEkqqKZo/Nyz8c9QkiRJhWWxK0mSpIZlG4MkSVJBeVMJSZIkqY6Z7EqSJBWUS49JkiRJdcxkV5IkqaC8XbAkSZJUx0x2JUmSCsqeXUmSJKmOmexKkiQVlD27kiRJUh0z2ZUkSSqoiMbPPRv/DCVJklRYJruSJEkF5WoMkiRJUh0z2ZUkSSooV2OQJEmS6pjFriRJkhqWbQySJEkFFbYxSJIkSfXLZFeSJKmgmlx6TJIkSapfJruSJEkFZc+uJEmSVMdMdiVJkgoqovFzz8Y/Q0mSJBWWya4kSVJBuRqDJEmSVMdMdiVJkgrK1RgkSZKkOmayK0mSVFBhz64kSZJUv0x2JUmSCsqeXUmSJKmOWexKkiSpYdnGIEmSVFDeVEKSJEmqYya7kiRJBRXR+Lln45+hJEmSCstkV5IkqaC8qYQkSZJUx0x2JUmSCsqbSkiSJEl1zGRXkiSpoOzZlSRJkuqYya4kSVJB2bMrSZIk1TGTXUmSpIJqsmdXkiRJql89kuzucuWRPfEyUq/29m3P1noKUk0tPWT9Wk9Bqqn8w6RaT2Eh9uxKkiRJdcxiV5IkSQ3LC9QkSZIKKgqQezb+GUqSJKmwTHYlSZIKygvUJEmSpDpmsitJklRQ4U0lJEmSpPplsitJklRQTfbsSpIkSfXLZFeSJKmg7NmVJEmS6pjJriRJUkG5zq4kSZJUx0x2JUmSCioKkHs2/hlKkiSpsEx2JUmSCsqeXUmSJKmOWexKkiSpYdnGIEmSVFBN3lRCkiRJql8mu5IkSQXlBWqSJElSHTPZlSRJKqiwZ1eSJEnqGRExJCKeiYjnIuLbbez/QkQ8Uf74U0Rs0dExTXYlSZIKqjf17EZEM3AxsAcwCRgXEWMy86mKYS8Au2TmGxGxFzAc2L6945rsSpIkqTfYDnguM5/PzPeAUcDQygGZ+afMfKO8+TCwekcHNdmVJEkqqOjB3DMihgHDKh4anpnDK7YHAxMrtifRfmp7FHBrR69rsStJkqSqKxe2w9sZ0lZPRbY5MGI3SsXuTh29rsWuJElSQTX1op5dSknuGhXbqwOvtB4UEZsDlwF7ZeZrHR3Unl1JkiT1BuOA9SJi7YhYEjgEGFM5ICLWBG4AvpSZz3bmoCa7kiRJBdWb1tnNzDkRcQJwO9AMXJ6ZT0bEceX9lwBnACsBvyyvJDEnM7dp77gWu5IkSeoVMnMsMLbVY5dUfH40cHRXjmmxK0mSVFC9aZ3darFnV5IkSQ3LZFeSJKmgelPPbrWY7EqSJKlhWexKkiSpYdnGIEmSVFBeoCZJkiTVMZNdSZKkgmoqQO7Z+GcoSZKkwjLZlSRJKih7diVJkqQ6ZrIrSZJUUN5UQpIkSapjJruSJEkFZc+uJEmSVMdMdiVJkgrKnl1JkiSpjpnsSpIkFZTJriRJklTHTHYlSZKKytUYJEmSpPplsStJkqSGZRuDJElSQXmBmiRJklTHTHYlSZIKytsFS5IkSXXMZFeSJKmg7NmVJEmS6pjJriRJUkGZ7EqSJEl1zGRXkiSpoFyNQZIkSapjJruSJEkFZc+uJEmSVMdMdiVJkgrKZFeSJEmqYya7kiRJBeVqDJIkSVIds9iVJElSw7KNQZIkqaC8QE2SJEmqYya7kiRJBeUFapIkSVIdM9mVJEkqKHt2JUmSpDpmsitJklRQJruSJElSHTPZlSRJKihXY6gQEStXcyKSJElSd+uw2I2Iz0XEVGB8REyKiI/3wLwkSZJUZdGD/9VKZ5Ld7wOfzMxVgQOA86o7JUmSJKl7dKZnd05m/gMgMx+JiH5VnpMkSZJ6QBFWY+hMsTswIk5a1HZm/qT7p6XO2nHwlpy8w1doamrixmfu5MonRi80ZutVNuGkHb5MS1ML0995k2PHngHAmIN+xez332ZufsDcD+Zy+JhTenr6UrfITM7/wQU8cN+D9Fm6D9/7wdlstPFGC4275upRXD1iJBMnTuSeB+9ihRVWAOCF51/gjNPP5Omn/sGJXz+BI75yeE+fglRVv/nmj9hn+08zZfo0Nhv26VpPR+pRnSl2fw30a2dbNdIUTZzy8WM4/rZzmDzrNUbsez73TRjHC9MnzR/Td8llOOXjx3Di7ecyedY0VujTf4FjHDv2TGa8O7Onpy51qwfue4AJL03g5ttuYvwT4zn37B9w9bVXLTRuy49tyc677szRRxy9wOP9l1uOU047hbvvvLunpiz1qCvu+B2/uOkKRnzrp7WeinqZIqzG0GGxm5lnL2pfRCzbvdNRV2wyYF0mvvkqL8+cDMAdzz/ALmtuu0CxO2SdT3L3S48wedY0AN54582azFWqprvvupfPDd2HiGDzLTZn5syZTJ06lQEDBiwwbqONN2zz+SuttCIrrbQi9997f09MV+px949/hLUGrV7raUg10amlxyJicERsExFLlrcHRsQPgH9WdXZq18BlVpxfxAJMmf06A5ddaYExa/ZfjX5LLsule5/NVUMv4LPr7jJ/X5JcPOQMrhp6AftvsEePzVvqblOmTGHQKqvM3x40aBBTJk+p4YwkSb1Fh8luRHwDOB14DlgqIn4G/AQYAWzdzvOGAcMA1vzSxxiwy9rdMV8tYOG3HjJzge2WpmY2Wnkd/uvWs1iqeUl++7nzGD/lWSa8+W+OuuV0ps1+gxX69OfiIWfy4oyXeezVp3pq8lL3afV1D8V4a06SFl/j/6zsTM/uMGCDzHw9ItakVPTunJkPt/ekzBwODAfY5jcHLPybSIttyuzXGLTsf+71MXCZFZk6+/UFxkye9RrT33mTd+a8yztz3uWxV59ivRU/woQ3/8202W8ApdaGe156hE1WXtdiV3Vj1MhrueF3NwCwyWabMPnVV+fvmzx5MgMGDljUUyVJBdKZNoZ3MvN1gMycADzbUaGrnvHU1OdYo/+qrNZ3IC1NLez50Z24b8KjC4y596U/s+UqG9EcTSzVvCSbDlyPF2dMok/LUiyzRB8A+rQsxfaDt+Bfb0yoxWlIH8ohhx3MdaOv5brR17Lb7rtx8023kJk88bcn6Nuv70L9upKkhUVEj33USmeS3dUj4qKK7YGV25n5te6fljpjbn7AhQ9dxs+HfJfmaGLMs3fx/PSJHLDhngBc/487eHHGyzw06XGu2f8nJMmNz/yRf70xkcH9BnHh7t8CoLmpmdv/dT8Pvfx4Dc9G+vA+ufNOPHDfA+wzZF/69OnDOd8/a/6+4489gTO/dwYDBw7k6qtGcsXlV/LatNf4/H4HsdPOO3HW985k2tRpHHrQF5j11iyamoL/e9XVjL75evr27Vu7k5K60cjTfsGum+/IysutyMSR4zhzxI+5/LZRtZ6W1COidY/nQgMijmhvf2Ze2dGL2MYgwQNHLrwUllQkSw9Zv9ZTkGoq/zCp1zXIPj/zmR6r0T7ab4OanH9nlh7rsJiVJEmSeqPOrMYwpr39mblv901HkiRJPcXbBZfsCEwErgEeoQhrVEiSJKkhdKbYXQXYAzgUOAz4f8A1mflkNScmSZKk6irCmuQdLj2WmXMz87bMPALYgdI6u/dExIlVn50kSZK0GDqT7BIRSwGfpZTufgS4CLihetOSJElStdmzC0TElcCmwK3A2Zn596rPSpIkSeoGnUl2vwTMAtYHvlbR2xFAZmb/Ks1NkiRJVWSyC2RmZ24pLEmSJPU6nerZlSRJUuNxNQZJkiSpjlnsSpIkqWHZxiBJklRQRbhAzWRXkiRJDctkV5IkqaC8QE2SJEmqYya7kiRJBWXPriRJklTHTHYlSZIKy2RXkiRJqlsmu5IkSQXV+Lmuya4kSZIamMmuJElSQbnOriRJklTHTHYlSZIKy2RXkiRJqlsmu5IkSQXV+Lmuya4kSZJ6iYgYEhHPRMRzEfHtNvZHRFxU3v9ERGzV0TEtdiVJklRzEdEMXAzsBWwMHBoRG7cathewXvljGPCrjo5rsStJklRY0YMfHdoOeC4zn8/M94BRwNBWY4YCI7LkYWD5iFi1vYNa7EqSJKnqImJYRDxa8TGs1ZDBwMSK7Unlx7o6ZgFeoCZJklRQPXlTicwcDgxvZ0hbk8kPMWYBJruSJEnqDSYBa1Rsrw688iHGLMBiV5IkSb3BOGC9iFg7IpYEDgHGtBozBji8vCrDDsCMzPx3ewe1jUGSJEk1l5lzIuIE4HagGbg8M5+MiOPK+y8BxgJ7A88Bs4Evd3Rci11JkqSCil52W4nMHEupoK187JKKzxM4vivHtI1BkiRJDctkV5IkqaB6W7JbDSa7kiRJalgWu5IkSWpYFruSJElqWPbsSpIkFVRP3kGtVkx2JUmS1LAsdiVJktSwLHYlSZLUsCx2JUmS1LC8QE2SJKmgvKmEJEmSVMdMdiVJkgrLZFeSJEmqWya7kiRJBdX4ua7JriRJkhqYya4kSVJBebtgSZIkqY6Z7EqSJBWWya4kSZJUt0x2JUmSCqrxc12TXUmSJDUwk11JkqTCavxs12RXkiRJDctkV5IkqaBcZ1eSJEmqYxa7kiRJalgWu5IkSWpYFruSJElqWF6gJkmSVFDh0mOSJElS/TLZlSRJKiyTXUmSJKlumexKkiQVVOPnuia7kiRJamAmu5IkSQXl7YIlSZKkOmayK0mSVFgmu5IkSVLdMtmVJEkqqMbPdU12JUmS1MBMdiVJkgqr8bNdk11JkiQ1LItdSZIkNSzbGCRJkgrKm0pIkiRJdcxiV5IkSQ3LYleSJEkNy55dSZKkggqXHpMkSZLqV2RmreegHhARwzJzeK3nIdWK3wOS3wcqJpPd4hhW6wlINeb3gOT3gQrIYleSJEkNy2JXkiRJDctitzjs0VLR+T0g+X2gAvICNUmSJDUsk11JkiQ1LItdSZIkNSyLXUmS6lxEZERcVbHdEhFTI+KW8vaR5e3HI+IfEfHfFWPPioiXy/v+HhH71uIcpGqx2O1FImJuxQ+bmyNi+Vb7/xYR17R67IqImB0R/Soe+1n5B9/K7bzW6RHxZEQ8UX7N7cuPXxYRG3fzqUnztfW1FxHfiIhlaj23zoiIsa2/N6VeYBawaUQsXd7eA3i51ZhrM3NL4BPA6RGxRsW+/y3v+zxweURYH6hh+MXcu7ydmVtm5qbA68Dx83ZExEaU/n/tHBHLtnrec8DQ8rgmYDcW/iE3X0TsCOwDbJWZmwOfBiYCZObRmflU952S9B/tfO19A+hSsRsRzd0+wU7IzL0zc3otXlvqwK3AZ8ufHwpc09agzHyN0u+NVdvY9zQwB1hkWCLVG4vd3ushYHDF9mHAVcAdQOu3mK4BDi5/vivwIKUfVouyKjAtM98FyMxpmfkKQETcExHbRMS+5dTt8Yh4JiJeKO/fOiLujYi/RMTtEbHQD0upHQt97QEHAqsBd0fE3QARcWhEjC+/y3H+vCdHxFsRcU5EPALsGBFnRMS48rjhERHlcduWk+OHIuLCiPh7+fHm8va48v5jFzXRiFg1Iu6reLflk+XHX4yIlSPiuIrvkRcq5r5n+XX/GhG/i4i+VfmblBY2CjgkIvoAmwOPtDUoItYE+gBPtLFve+ADYGoV5yn1KIvdXqicWO0OjKl4+GDgWkqF7aGtnvJPYEBErFDeN6qDl7gDWCMino2IX0bELq0HZOaYcsq8JfA34EcRsQTwc+DAzNwauBz4fpdPUEW20NdeZl4EvALslpm7RcRqwPnAp4AtgW0jYr/y85cF/p6Z22fmA8AvMnPb8rshS1NKjQF+CxyXmTsCcyte/yhgRmZuC2wLHBMRay9irocBt5e/B7YAHq/cmZmXlPdtC0wCflJuHfoO8OnM3Ap4FDipy39L0oeQmU8AH6H0e2BsG0MOjogngeeBn2XmOxX7/jsiHgd+BBycrkuqBmKx27ssXf5h8xqwIvAHKKVUwNTMfAm4E9iqXNhWugE4BNgeuL+9F8nMt4CtKd0jfSpwbUQc2dbYiPgWpfaKi4ENgE2BP5Tn+R1g9S6fpQqrk1972wL3ZObUzJwDXA3sXN43F7i+YuxuEfFIRIynVBxvUu6n7ZeZfyqPGVkxfk/g8PLX7yPASsB6i5juOODLEXEWsFlmzlzEuJ8Bd2XmzcAOwMbAg+XXOAJYaxHPk6phDKWCta0WhmszcxPgk8CPI2KVin3/Ww44PpmZ7f4OkepNS60noAW8nZlbRsRywC2UenYvovSv9A0j4sXyuP7AAcBlFc8dBfwVuDIzPyi/m7tImTkXuAe4p1woHAFcUTkmInandLHCvEIjgCfLaZn0oSzia69Se1+875SfT/mt2l8C22TmxHJR2qeD5wdwYmbe3ol53hcRO1PqgbwqIi7MzBELHKxUqK8FnFBx/D9kZut3X6Secjmldy/GR8SubQ3IzIeitHLD14FTe3BuUk2Y7PZCmTkD+BpwckQsRang3DwzP5KZH6F0MdqhrZ4zATid0i//dkXEBhFRmWZtCbzUasxa5WMdlJlvlx9+hlK7xI7lMUtExCZdP0MVVTtfezOBeSuKPALsUu6Lbab0tX5vG4frU/5zWrkv9kCAzHwDmBkRO5T3H1LxnNuB/yq35BAR67dxwee8ua4FTMnMXwO/AbZqtX9r4GTgi5n5Qfnhh4FPRMS65THLRMT6i/wLkbpZZk7KzJ91Yuj5lN656NfhSKnOmez2Upn5WET8DTgIeDkzK1dXuA/YuPXFYZl5aScP3xf4efnt3jmUrsod1mrMkZTe4h1dTolfycy9I+JA4KJy+twC/BR4sgunpmJb1NfeocCtEfHvct/uqcDdlJLSsZl5U+sDZeb0iPg1MB54kVLbwTxHAb+OiFmUUuQZ5ccvo9TT+NfyxWxTgf0WMdddgf+JiPeBt4DDW+0/gVK70d3l75FHM/Poctp7TfkfqlBq93m2vb8UaXFl5kIXQmbmPZS+/snMK6h49658UfK8Noazqjw9qabCHnRJjSYi+pb7g4mIbwOrZubXazwtSVINmOxKakSfLafDLZTaJI6s7XQkSbVistvAImIlSqs3tLZ7eVFxqfAiYjNKa1hXejczt6/FfCRJ3ctiV5IkSQ3L1RgkSZLUsCx2JUmS1LAsdiVJktSwLHYlSZLUsP4/Zj17Hql0eroAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 936x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Co-relation b/w Price and other numerical features \n",
    "plt.figure(figsize = (13,10))\n",
    "sns.heatmap(df_new.corr(), cmap=\"Greens\" , annot= True)\n",
    "\n",
    "#Observation : Ram_size has most correlation b/w price 65%"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "a789c9ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Average Price of Laptop as per the  Brand')"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Average Price as per Brand\n",
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(data=df, x=\"Brand_name\", y=\"MRP\" );\n",
    "plt.ylabel(\"Average MRP\")\n",
    "plt.title(\"Average Price of Laptop as per the  Brand\")\n",
    "\n",
    "#Observation : \"Alienware\" is the most expensive one "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c603a58",
   "metadata": {},
   "source": [
    "### Summary of insights\n",
    "- ALienware is the most expensive laptops with avg of 2-3.5 lakhs\n",
    "- The more the storage size the higher the price\n",
    "- Higher the Ram size the higher the price\n",
    "- Higher the Storage size the more expensive the laptop is . "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed134d9c",
   "metadata": {},
   "source": [
    "### Building a Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "559972f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>Processor</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "      <th>MRP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>256</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>36990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lenovo</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>39990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>32990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HP</td>\n",
       "      <td>AMD</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS</td>\n",
       "      <td>Intel</td>\n",
       "      <td>8</td>\n",
       "      <td>DDR4</td>\n",
       "      <td>512</td>\n",
       "      <td>SSD</td>\n",
       "      <td>Windows</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Brand_name Processor  RAM_Size RAM_Type  Storage_size Storage_type  OS_Type  \\\n",
       "0     Lenovo     Intel         8     DDR4           256          SSD  Windows   \n",
       "1     Lenovo     Intel         8     DDR4           512          SSD  Windows   \n",
       "2       ASUS     Intel         8     DDR4           512          SSD  Windows   \n",
       "3         HP       AMD         8     DDR4           512          SSD  Windows   \n",
       "4       ASUS     Intel         8     DDR4           512          SSD  Windows   \n",
       "\n",
       "       MRP  \n",
       "0  36990.0  \n",
       "1  39990.0  \n",
       "2  32990.0  \n",
       "3  49990.0  \n",
       "4  49990.0  "
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_new.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "d8f3bc45",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Encoding the colums \n",
    "from sklearn.preprocessing import OrdinalEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "4c83276f",
   "metadata": {},
   "outputs": [],
   "source": [
    "enc = OrdinalEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "f013de30",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\bhask\\AppData\\Local\\Temp\\ipykernel_23360\\3957059412.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df_new[['Brand_name','Processor','RAM_Type','Storage_type','OS_Type']] = enc.fit_transform(df_new[['Brand_name','Processor','RAM_Type','Storage_type','OS_Type']])\n"
     ]
    }
   ],
   "source": [
    "df_new[['Brand_name','Processor','RAM_Type','Storage_type','OS_Type']] = enc.fit_transform(df_new[['Brand_name','Processor','RAM_Type','Storage_type','OS_Type']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "59748afe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 421 entries, 0 to 719\n",
      "Data columns (total 8 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   Brand_name    421 non-null    float64\n",
      " 1   Processor     421 non-null    float64\n",
      " 2   RAM_Size      421 non-null    int64  \n",
      " 3   RAM_Type      421 non-null    float64\n",
      " 4   Storage_size  421 non-null    int64  \n",
      " 5   Storage_type  421 non-null    float64\n",
      " 6   OS_Type       421 non-null    float64\n",
      " 7   MRP           421 non-null    float64\n",
      "dtypes: float64(6), int64(2)\n",
      "memory usage: 29.6 KB\n"
     ]
    }
   ],
   "source": [
    "df_new.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "38b7311a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>Processor</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "      <th>MRP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>256</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>36990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>39990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>32990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>49990.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Brand_name  Processor  RAM_Size  RAM_Type  Storage_size  Storage_type  \\\n",
       "0         7.0        1.0         8       0.0           256           1.0   \n",
       "1         7.0        1.0         8       0.0           512           1.0   \n",
       "2         2.0        1.0         8       0.0           512           1.0   \n",
       "3         5.0        0.0         8       0.0           512           1.0   \n",
       "4         2.0        1.0         8       0.0           512           1.0   \n",
       "\n",
       "   OS_Type      MRP  \n",
       "0      2.0  36990.0  \n",
       "1      2.0  39990.0  \n",
       "2      2.0  32990.0  \n",
       "3      2.0  49990.0  \n",
       "4      2.0  49990.0  "
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_new.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "2e866d1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# SPlitting the data into train and test\n",
    "X = df_new.iloc[: , :-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "id": "c81d2f2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>Processor</th>\n",
       "      <th>RAM_Size</th>\n",
       "      <th>RAM_Type</th>\n",
       "      <th>Storage_size</th>\n",
       "      <th>Storage_type</th>\n",
       "      <th>OS_Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>256</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>713</th>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>16</td>\n",
       "      <td>1.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>714</th>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>16</td>\n",
       "      <td>0.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>715</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>718</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>16</td>\n",
       "      <td>5.0</td>\n",
       "      <td>512</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>719</th>\n",
       "      <td>7.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>256</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>421 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Brand_name  Processor  RAM_Size  RAM_Type  Storage_size  Storage_type  \\\n",
       "0           7.0        1.0         8       0.0           256           1.0   \n",
       "1           7.0        1.0         8       0.0           512           1.0   \n",
       "2           2.0        1.0         8       0.0           512           1.0   \n",
       "3           5.0        0.0         8       0.0           512           1.0   \n",
       "4           2.0        1.0         8       0.0           512           1.0   \n",
       "..          ...        ...       ...       ...           ...           ...   \n",
       "713         3.0        1.0        16       1.0           512           1.0   \n",
       "714         5.0        0.0        16       0.0           512           1.0   \n",
       "715         2.0        1.0         4       3.0             1           1.0   \n",
       "718         2.0        1.0        16       5.0           512           1.0   \n",
       "719         7.0        1.0         8       0.0           256           0.0   \n",
       "\n",
       "     OS_Type  \n",
       "0        2.0  \n",
       "1        2.0  \n",
       "2        2.0  \n",
       "3        2.0  \n",
       "4        2.0  \n",
       "..       ...  \n",
       "713      2.0  \n",
       "714      2.0  \n",
       "715      1.0  \n",
       "718      2.0  \n",
       "719      2.0  \n",
       "\n",
       "[421 rows x 7 columns]"
      ]
     },
     "execution_count": 249,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "724aa2e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "Y = df_new.iloc[ : ,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "id": "df6fa2b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       36990.0\n",
       "1       39990.0\n",
       "2       32990.0\n",
       "3       49990.0\n",
       "4       49990.0\n",
       "         ...   \n",
       "713     76590.0\n",
       "714     90000.0\n",
       "715     23490.0\n",
       "718    125990.0\n",
       "719     50990.0\n",
       "Name: MRP, Length: 421, dtype: float64"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "4fc20855",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train , x_test , y_train , y_test = train_test_split( X, Y, test_size = 0.25, random_state=100 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "id": "8093ff3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shape of x_train (315, 7)\n",
      "shape of x_test (106, 7)\n",
      "shape of y_train (315,)\n",
      "shape of y_test (106,)\n"
     ]
    }
   ],
   "source": [
    "print(\"shape of x_train\" ,x_train.shape)\n",
    "print(\"shape of x_test\" ,x_test.shape)\n",
    "print(\"shape of y_train\",y_train.shape)\n",
    "print(\"shape of y_test\",y_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3e079f7",
   "metadata": {},
   "source": [
    "### Linear_Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "id": "645231e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "Lin_reg = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "id": "96f67668",
   "metadata": {},
   "outputs": [],
   "source": [
    "Lin_reg = Lin_reg.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "id": "8fdc1eb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = Lin_reg.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "id": "b4ba673f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import  r2_score,  mean_squared_error as mse\n",
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "id": "3fe90faa",
   "metadata": {},
   "outputs": [],
   "source": [
    "evaluation = pd.DataFrame({\"Model\" : ['Linear Regression'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "7dcb2fe9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60d9e5ce",
   "metadata": {},
   "source": [
    "### K_Nearest "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "id": "b111795b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "knn = KNeighborsRegressor( n_neighbors=3 )\n",
    "knn = knn.fit( x_train,y_train )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "6d5d2814",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = knn.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "id": "4dc9fd62",
   "metadata": {},
   "outputs": [],
   "source": [
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)\n",
    "evaluation_knn = pd.DataFrame({\"Model\" : ['KNN'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )\n",
    "evaluation = pd.concat([evaluation, evaluation_knn])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "id": "cef4ad19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KNN</td>\n",
       "      <td>5.436663e+08</td>\n",
       "      <td>23316.652554</td>\n",
       "      <td>0.733818</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709\n",
       "0                KNN  5.436663e+08  23316.652554  0.733818"
      ]
     },
     "execution_count": 263,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae78dc92",
   "metadata": {},
   "source": [
    "### RRandom_Forest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "id": "5a2ce2c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "c0397b1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "rf=RandomForestRegressor(n_estimators = 10, max_depth = 12, random_state = 3)\n",
    "rf.fit(x_train,y_train)\n",
    "y_pred=rf.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "id": "c26c2d02",
   "metadata": {},
   "outputs": [],
   "source": [
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)\n",
    "evaluation_ran = pd.DataFrame({\"Model\" : ['Random_Forest'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )\n",
    "evaluation = pd.concat([evaluation, evaluation_ran])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "id": "eb56258e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KNN</td>\n",
       "      <td>5.436663e+08</td>\n",
       "      <td>23316.652554</td>\n",
       "      <td>0.733818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random_Forest</td>\n",
       "      <td>4.390364e+08</td>\n",
       "      <td>20953.195137</td>\n",
       "      <td>0.785045</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709\n",
       "0                KNN  5.436663e+08  23316.652554  0.733818\n",
       "0      Random_Forest  4.390364e+08  20953.195137  0.785045"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e6a1bd4",
   "metadata": {},
   "source": [
    "### Decision_Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "id": "87a3437d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "id": "878cf09b",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt=DecisionTreeRegressor()\n",
    "dt.fit(x_train,y_train)\n",
    "y_pred=dt.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "id": "aa88c143",
   "metadata": {},
   "outputs": [],
   "source": [
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)\n",
    "evaluation_dec = pd.DataFrame({\"Model\" : ['Decision_Tree'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )\n",
    "evaluation = pd.concat([evaluation, evaluation_dec])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "id": "643d6175",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KNN</td>\n",
       "      <td>5.436663e+08</td>\n",
       "      <td>23316.652554</td>\n",
       "      <td>0.733818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random_Forest</td>\n",
       "      <td>4.390364e+08</td>\n",
       "      <td>20953.195137</td>\n",
       "      <td>0.785045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Decision_Tree</td>\n",
       "      <td>5.984249e+08</td>\n",
       "      <td>24462.725525</td>\n",
       "      <td>0.707007</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709\n",
       "0                KNN  5.436663e+08  23316.652554  0.733818\n",
       "0      Random_Forest  4.390364e+08  20953.195137  0.785045\n",
       "0      Decision_Tree  5.984249e+08  24462.725525  0.707007"
      ]
     },
     "execution_count": 271,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1ce5d5c",
   "metadata": {},
   "source": [
    "### ADA_Boost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "id": "fcf2de50",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import AdaBoostRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "77cb7fdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "ada_boost=AdaBoostRegressor(n_estimators=100,learning_rate=0.001,random_state=0)\n",
    "ada_boost.fit(x_train,y_train)\n",
    "y_pred=ada_boost.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "id": "edbcf5bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)\n",
    "evaluation_ada = pd.DataFrame({\"Model\" : ['ADA_Boost'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )\n",
    "evaluation = pd.concat([evaluation, evaluation_ada])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "99358d61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KNN</td>\n",
       "      <td>5.436663e+08</td>\n",
       "      <td>23316.652554</td>\n",
       "      <td>0.733818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random_Forest</td>\n",
       "      <td>4.390364e+08</td>\n",
       "      <td>20953.195137</td>\n",
       "      <td>0.785045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Decision_Tree</td>\n",
       "      <td>5.984249e+08</td>\n",
       "      <td>24462.725525</td>\n",
       "      <td>0.707007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ADA_Boost</td>\n",
       "      <td>5.365907e+08</td>\n",
       "      <td>23164.426439</td>\n",
       "      <td>0.737282</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709\n",
       "0                KNN  5.436663e+08  23316.652554  0.733818\n",
       "0      Random_Forest  4.390364e+08  20953.195137  0.785045\n",
       "0      Decision_Tree  5.984249e+08  24462.725525  0.707007\n",
       "0          ADA_Boost  5.365907e+08  23164.426439  0.737282"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2b15675",
   "metadata": {},
   "source": [
    "### XG_Boost\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "aca7de88",
   "metadata": {},
   "outputs": [],
   "source": [
    "from xgboost import XGBRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "92023528",
   "metadata": {},
   "outputs": [],
   "source": [
    "xgb=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=98) \n",
    "xgb.fit(x_train,y_train)\n",
    "y_pred=xgb.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "id": "25c8dc82",
   "metadata": {},
   "outputs": [],
   "source": [
    "MSE = mse (y_test, y_pred)\n",
    "RMSE = np.sqrt(MSE)\n",
    "R2 = r2_score(y_test, y_pred)\n",
    "evaluation_xg = pd.DataFrame({\"Model\" : ['XG_Boost'], \"MSE\" : [MSE], 'RMSE':[RMSE] , 'R2_Score': [R2]} )\n",
    "evaluation = pd.concat([evaluation, evaluation_xg])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "id": "ef9555c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>1.252622e+09</td>\n",
       "      <td>35392.401097</td>\n",
       "      <td>0.386709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KNN</td>\n",
       "      <td>5.436663e+08</td>\n",
       "      <td>23316.652554</td>\n",
       "      <td>0.733818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random_Forest</td>\n",
       "      <td>4.390364e+08</td>\n",
       "      <td>20953.195137</td>\n",
       "      <td>0.785045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Decision_Tree</td>\n",
       "      <td>5.984249e+08</td>\n",
       "      <td>24462.725525</td>\n",
       "      <td>0.707007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ADA_Boost</td>\n",
       "      <td>5.365907e+08</td>\n",
       "      <td>23164.426439</td>\n",
       "      <td>0.737282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>XG_Boost</td>\n",
       "      <td>4.131576e+08</td>\n",
       "      <td>20326.277380</td>\n",
       "      <td>0.797716</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>XG_Boost</td>\n",
       "      <td>3.566053e+08</td>\n",
       "      <td>18883.995481</td>\n",
       "      <td>0.825404</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model           MSE          RMSE  R2_Score\n",
       "0  Linear Regression  1.252622e+09  35392.401097  0.386709\n",
       "0                KNN  5.436663e+08  23316.652554  0.733818\n",
       "0      Random_Forest  4.390364e+08  20953.195137  0.785045\n",
       "0      Decision_Tree  5.984249e+08  24462.725525  0.707007\n",
       "0          ADA_Boost  5.365907e+08  23164.426439  0.737282\n",
       "0           XG_Boost  4.131576e+08  20326.277380  0.797716\n",
       "0           XG_Boost  3.566053e+08  18883.995481  0.825404"
      ]
     },
     "execution_count": 283,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80978c2f",
   "metadata": {},
   "source": [
    "### As  we can from above , XG_Boost has highest R2 score and lowest RMSE . SO , we select this model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de29a8a2",
   "metadata": {},
   "source": [
    "#### Lets see if applying cross validation improves permorfance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "a15cb7fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import cross_val_score, KFold, ShuffleSplit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "c0596806",
   "metadata": {},
   "outputs": [],
   "source": [
    "xgb=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=98)\n",
    "\n",
    "k=ShuffleSplit(n_splits=20, test_size=0.2, random_state=10)\n",
    "score=cross_val_score(xgb, X,Y, cv=k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 289,
   "id": "e8c90bea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cross validations Score:\n",
      " [0.80722289 0.68707252 0.80706274 0.69160678 0.79020249 0.8240916\n",
      " 0.66864715 0.84030239 0.83657762 0.84668153 0.78769302 0.68331002\n",
      " 0.66977541 0.68328111 0.81131788 0.87775017 0.66273121 0.86496929\n",
      " 0.71171316 0.82930513]\n",
      "----------------------------------------------\n",
      "Cross validations Score Maximum : 0.8777501712852432\n",
      "Cross validations Score Minimum: 0.6627312087627302\n",
      "Cross validations Score Average: 0.7690657054790686\n"
     ]
    }
   ],
   "source": [
    "print(\"Cross validations Score:\\n\", score)\n",
    "print(\"----------------------------------------------\")\n",
    "print(\"Cross validations Score Maximum :\", score.max())\n",
    "print(\"Cross validations Score Minimum:\", score.min())\n",
    "print(\"Cross validations Score Average:\", score.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28643245",
   "metadata": {},
   "source": [
    "#### But as we can see Cross validation did not improve model performance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f53e883c",
   "metadata": {},
   "source": [
    "#### Save the Model \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 290,
   "id": "b186ff8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "pickle_out = open(\"xgb.pkl\",\"wb\")\n",
    "pickle.dump(xgb, pickle_out)\n",
    "pickle_out.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fb8dfaa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
