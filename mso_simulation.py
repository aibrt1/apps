import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install('numpy')
import_or_install('matplotlib')
import_or_install('rich')

import numpy as np
import matplotlib.pyplot as plt
from rich import print


def dSHASHo(x, mu = 0, sigma = 1, nu = 0, tau = 1):
    z = (x - mu)/sigma
    c = np.cosh(tau * np.arcsinh(z) - nu)
    r = np.sinh(tau * np.arcsinh(z) - nu)
    loglik = -np.log(sigma) + np.log(tau) - 0.5 * np.log(2 * np.pi) - 0.5 * np.log(1 + (z**2)) + np.log(c) - 0.5 * (r**2)
    result = np.exp(loglik)
    return result

#link: https://github.com/aibrt1/

x = np.linspace(0, 18, 10000)

print("**************************************************\n****************** [blink][italic purple]Welcome to Bisexuality Theory![/italic purple] ********************** \n**************************************************\n\n" +\
      "This app will allow you to apply Bisexuality Theory (Epstein et al., 2021) to a set of hypothetical scores on the Epstein Sexual Orientation Inventory (ESOI), which is accessible at https://MySexualOrientation.com. It will allow you to simulate what happens when social pressure ([italic]S[/italic]) is applied to a population, pushing the members of that population to be either opposite-sex (OS) attracted ('straight') or same-sex (SS) attracted ('gay').\n\n" +\
      "Values of [italic]S[/italic] greater than 0 push the distribution to the left, toward OS attraction. Values less than 0 push the distribution to the right, toward SS attraction. As we explain in a recent publication (link to be posted here soon), when social pressure exceeds a certain value, the skewed distribution breaks, yielding a second mode. This creates the impression that there are two different types of people, the OS attracted ('straight' or 'heterosexual') and the SS attracted ('gay' or 'homosexual'). In fact, everyone is a mix of OS and SS tendencies, and the bimodal distibution is a distortion of a relatively normal curve. That distortion is produced by extreme social pressure. In theory, that pressure could be applied in either direction: toward exclusive OS attraction, or toward exclusive SS attraction.\n\n" +\
      "Our computational model derives from a linear combination of two sinh-arcsinh distributions at certain mixture rates. It contains eight parameters, each of which has been estimated from data obtained from a group of 1.2 million people in 219 countries and territories. Feel free to change any of the parameters to explore how our computational model works. For details, please see the publication mentioned above. If you would like to contact the authors to suggest improvements to the model, please write to us at: info@aibrt.org. \n\n" +\
      "[bold cyan]You can now conduct your simulation. Please choose any social pressure level ([italic]S[/italic]) between[/bold cyan] [bold white on cyan]-1 and +1 [/bold white on cyan]\n" +\
      "[bold yellow]\nIf you want to exit the app, please type [bold white on yellow]'quit'[/bold white on yellow] and hit ENTER.[/bold yellow]")
while True:
    S = input("\nPlease choose a value for S = ")
    if S == "quit":
        break
    else:
        try:
            s = float(S)
        except:
            print('[bold red]Input cannot be recognized. Please input any number between [bold white on red]-1 and +1[/bold white on red], or type [bold white on red]"quit"[/bold white on red] to exit[/bold red]')
            continue
        if (s < -1) | (s > 1):
            print("[bold red]Input out of range! Please input any number between [bold white on red]-1 and +1[/bold white on red], or type [bold white on red]'quit'[/bold white on red] to exit[/bold red]" )
            continue

        p = 0.9257
        mu1 = 8.5222
        sigma1 = 1.5365
        nu1 = -0.0966
        tau1 = 0.5996
        mu2 = 13.9438
        sigma2 = 2.3168
        nu2 = -0.4763
        tau2 = 0.6

        if s < 0:
            mu2 = 5.2840

        s = float(S)
        mu1_ = mu1 - np.exp(abs(s)) ** 2 * s
        sigma1_ = sigma1 - abs(s)
        nu1_ = nu1 + s
        tau1_ = tau1

        mu2_ = mu2 + 2 * s
        sigma2_ = sigma2 - abs(2 * s)
        nu2_ = nu2 + s
        tau2_ = tau2
        print(round(mu1_, 2), round(sigma1_, 2), round(nu1_, 2), round(tau1_, 2), round(mu2_, 2), round(sigma2_, 2),
              round(nu2_, 2), round(tau2_, 2))
        y = p * dSHASHo(x, mu=mu1_, sigma=sigma1_,
                        nu=nu1_, tau=tau1_) + (1 - p) * dSHASHo(x, mu=mu2_, sigma=sigma2_, nu=nu2_, tau=tau2_)

        # temp = df_clean.mso.value_counts()
        # mu, sigma = 0, 0.2
        # noise2 = np.random.normal(mu, sigma, df_clean.shape[0])

        # colors = ['black', 'green', 'steelblue', 'lightblue', 'brown', 'red', 'darkslategrey', 'purple', 'grey',
        #           'darkorange', 'blue']
        colors = ['black', 'green', 'red', 'purple', 'blue', 'teal']
        fig, ax = plt.subplots(figsize=(12, 6))
        # plot the histgram
        # ax.plot(kde.support, kde.density, lw = 3, label = 'KDE from Mso values', zorder = 10)
        # ax.plot(x, y, color = 'blue', lw = 3)
        # ax.hist(df_clean.mso + noise2, density=True, bins=37, width=0.42, color='gray', alpha=0.2)

        ax.plot(x, y, label="$\mathregular{\mathit{S}}$ = %.2f" % (s), lw=3, color=np.random.choice(colors, 1)[0])
        ax.legend()

        ax.set_xticks(np.arange(0, 19, 1))
        ax.set_xticklabels(np.arange(0, 19, 1), fontsize=12)

        # ax.set_yticks([round(i, 2) for i in np.arange(0, 0.4, 0.05)])
        # ax.set_yticklabels(["0.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30", "0.35"], fontsize=12)

        plt.yticks(fontsize = 12)
        ax.set_ylabel('Probability Density', fontsize=12, fontweight='bold')
        ax.set_xlabel('Sexual Orientation Continuum', fontsize=12, fontweight='bold')
        ax.set_title("MSO Distribution with Different Levels of Social Pressure", fontsize=15, fontweight='bold')
        plt.show()
