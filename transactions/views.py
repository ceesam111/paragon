from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import DepositForm, WithdrawalForm


@login_required()
def deposit_view(request):
    form = DepositForm(request.POST or None)

    if form.is_valid():
        deposit = form.save(commit=False)
        deposit.user = request.user
        deposit.save()
        # adds users deposit to balance.
        deposit.user.account.balance += deposit.amount
        deposit.user.account.save()
        messages.success(request, 'You Have Deposited {} $.'
                         .format(deposit.amount))
        return redirect("home")

    context = {
        "title": "Deposit",
        "form": form
    }
    return render(request, "transactions/form.html", context)


@login_required()
def withdrawal_view(request):
	messages.success(
	request, 'Please text Withdrawal  with your Paragon Account Details (PAD) and amount to withdraw and the account details to recieve it(LAD). Text this message to 08108141473 or +2348057388145 or contact the admin for more information. This is for security reasons. Thanks for trusting us!')
	
	return redirect("home")
       
    #form = WithdrawalForm(request.POST or None, user=request.user)

  #  if form.is_valid():
        #withdrawal = form.save(commit=False)
      #  withdrawal.user = request.user
      #  withdrawal.save()
        # subtracts users withdrawal from balance.
        
        #totalwithdraw = withdrawal.amount + 100
     #   if totalwithdraw >= withdrawal.user.account.balance:
          #  messages.success(
      #      request, 'You cannot withdraw  {} $. with additional charges of #100'.format(withdrawal.amount))
        #    return redirect("home")
        
       # else:
    #    	withdrawal.user.account.balance -= totalwithdraw
   #     	withdrawal.user.account.save()
     #   	messages.success(
    #    	request, 'You Have Withdrawn {} $. with additional charges of #100'.format(withdrawal.amount))
     #   	return redirect("home")

#    context = {
     #   "title": "Withdraw",
#        "form": form
 #   }
  #  return render(request, "transactions/form.html", context)
