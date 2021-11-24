<template>
  <div class="purchase">
    <Header></Header>
    <row :gutter="12">
      <column :xs="12" :md="4" :lg="3"></column>
      <column :xs="12" :md="4" :lg="3">
        <b-col cols="">
          <div class="purchase-title-container">
            <div class="content-title">Purchase Dorks</div>
            <div class="content-text">
              This is a body of text where we talk about the price, what you get
              and how cool Dorks really is and maybe a little about buying for
              others too.
            </div>
          </div>
          <div class="purchase-title-container">
            <div v-if="subscription == 'Monthly'">
              <b-card style="background-color: #00b15c">
                <h4 align="left" style="color: white">Monthly Plan</h4>
                <b-container class="bv-example-row">
                  <b-row>
                    <b-col
                      ><p align="left" style="color: white">
                        Lorem ipsum dolor sit amet consectetur
                      </p></b-col
                    >
                    <b-col>
                      <b-form-radio
                        v-model="subscription"
                        name="some-radios"
                        value="Monthly"
                      ></b-form-radio>
                    </b-col>
                  </b-row>
                </b-container>

                <h2 class="context-text" align="left" style="color: white">
                  $19
                </h2>
              </b-card>
            </div>
            <div v-else>
              <b-card>
                <h4 align="left">Monthly Plan</h4>
                <b-container class="bv-example-row">
                  <b-row>
                    <b-col
                      ><p align="left">
                        Lorem ipsum dolor sit amet consectetur
                      </p></b-col
                    >
                    <b-col>
                      <b-form-radio
                        v-model="subscription"
                        name="some-radios"
                        value="Monthly"
                      ></b-form-radio>
                    </b-col>
                  </b-row>
                </b-container>

                <h2 class="context-text" align="left">$19</h2>
              </b-card>
            </div>

            <br />
            <div v-if="subscription == 'Yearly'">
              <b-card style="background-color: #00b15c">
                <h4 align="left" style="color: white">Yearly Plan</h4>
                <b-container class="bv-example-row">
                  <b-row>
                    <b-col
                      ><p align="left" style="color: white">
                        Lorem ipsum dolor sit amet consectetur
                      </p></b-col
                    >
                    <b-col>
                      <b-form-radio
                        v-model="subscription"
                        name="some-radios"
                        value="Yearly"
                      ></b-form-radio>
                    </b-col>
                  </b-row>
                </b-container>

                <h2 class="context-text" align="left" style="color: white">
                  $199
                </h2>
              </b-card>
            </div>
            <div v-else>
              <b-card>
                <h4 align="left">Yearly Plan</h4>
                <b-container class="bv-example-row">
                  <b-row>
                    <b-col
                      ><p align="left">
                        Lorem ipsum dolor sit amet consectetur
                      </p></b-col
                    >
                    <b-col>
                      <b-form-radio
                        v-model="subscription"
                        name="some-radios"
                        value="Yearly"
                      ></b-form-radio>
                    </b-col>
                  </b-row>
                </b-container>

                <h2 class="context-text" align="left">$199</h2>
              </b-card>
            </div>
          </div>
        </b-col></column
      >
      <column :xs="12" :md="4" :lg="3">
        <b-col cols="">
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />

          <div class="purchase-form-container">
            <form class="stripe-form">
              <div class="form-container" style="width: auto">
                <div class="input-element">
                  <label for="card-information">Card Information*</label>
                  <div
                    id="aio-card"
                    style="
                      height: auto;
                      border-radius: 10px;
                      width: 100%;
                      border: 1px solid;
                      padding-top: 15px;
                      padding-bottom: 15px;
                    "
                  ></div>
                  <!--<StripeElementCard :pk="publishableKey"></StripeElementCard>-->
                </div>
                <div class="input-element">
                  <label for="name-on-card">Name on card*</label>
                  <input
                    v-model="name_on_card"
                    type="text"
                    id="name-on-card-input"
                    placeholder="Name as it appears"
                    required
                  />
                </div>

                <!-------------55555555555------------>

                <div class="basic-addr-form" v-if="manualAddress == false">
                  <div class="input-element">
                    <label for="billing-address">Billing Address*</label>
                    <country-select
                      style="height: 50px; border-radius: 10px; width: 100%"
                      v-model="country"
                      :country="country"
                      topCountry="US"
                    />
                  </div>
                  <div class="input-element">
                    <input
                      v-model="address"
                      type="text"
                      id="address"
                      placeholder="Address"
                      required
                    />
                  </div>
                </div>

                <div class="complex-addr-form" v-else>
                  <div class="input-element">
                    <label for="last-name">Billing Address*</label>
                    <country-select
                      style="height: 50px; border-radius: 10px; width: 100%"
                      v-model="country"
                      :country="country"
                      topCountry="US"
                    />
                  </div>
                  <div class="input-element">
                    <input
                      v-model="addressLine1"
                      type="text"
                      id="address1"
                      placeholder="Address Line 1"
                      required
                    />
                  </div>
                  <div class="input-element">
                    <input
                      v-model="addressLine2"
                      type="text"
                      id="address2"
                      placeholder="Address Line 2"
                      required
                    />
                  </div>
                  <div class="input-element">
                    <input
                      v-model="city"
                      type="text"
                      id="city"
                      placeholder="City"
                      required
                    />
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="input-element">
                        <input
                          v-model="state"
                          type="text"
                          id="state"
                          placeholder="State"
                          required
                        />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="input-element">
                        <input
                          v-model="zipcode"
                          type="text"
                          id="zip"
                          placeholder="Zip"
                          required
                        />
                      </div>
                    </div>
                  </div>
                </div>
                <div v-if="manualAddress == false">
                  <a
                    href="#"
                    style="color: #00b15c"
                    @click.prevent="toggleAddressForm"
                    >Enter Address Manually</a
                  >
                </div>

                <br />
                <div>
                  <!-- <button
                  v-if="name_on_card != ''"
                  type="submit"
                  @click.prevent="makePayment"
                  class="purchase-button"
                  :disabled="false"
                >
                  Purchase Dorks
                </button>
                <button
                  v-else
                  type="submit"
                  class="purchase-button"
                  :disabled="checkout_disabled"
                >
                  Purchase Dorks
                </button>-->

                  <div v-if="checkout_error" class="checkout-error">
                    {{ checkout_error }}
                  </div>
                  <!--                <StripeElementCard pk="this.pk" :change="this.card_change" class="stripe-card"></StripeElementCard>-->
                  <button
                    v-if="checkout_loading"
                    type="submit"
                    class="purchase-button"
                    :disabled="this.checkout_disabled"
                  >
                    <font-awesome-icon
                      :icon="['fa', 'spinner']"
                      class="fa-spin"
                    ></font-awesome-icon>
                  </button>
                  <button
                    v-else
                    type="submit"
                    :disabled="checkout_disabled"
                    class="purchase-button"
                  >
                    Purchase Dorks
                  </button>
                </div>
                <br />
                <p>
                  By placing your order, you agree to our
                  <a href="#" style="color: #00b15c">terms of service</a> and
                  <a href="#" style="color: #00b15c">privacy policy</a>.<br />

                  By confirming, you allow Dorks, Inc. to charge your card for
                  this payment and future payments in accordance with their
                  terms.
                </p>
              </div>
            </form>
          </div>
        </b-col></column
      >
      <column :xs="12" :md="4" :lg="3"></column>
    </row>

    <div class="purchase-form-container"></div>

    <div v-if="is_mobile" class="dorks-container">
      <img
        :src="require('@/assets/img/dorks-couple-mobile.svg')"
        class="dorks dork-girl-hat"
        alt=""
      />
      <img
        :src="require('@/assets/img/dorks-single-mobile.svg')"
        class="dorks dork-guy-hat"
        alt=""
      />
    </div>
    <div v-else class="dorks-container">
      <img
        :src="require('@/assets/img/dorks-couple.svg')"
        class="dorks dork-girl-hat"
        alt=""
      />
      <img
        :src="require('@/assets/img/dorks-single.svg')"
        class="dorks dork-guy-hat"
        alt=""
      />
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import MonthlyPlan from "@/components/ui/MonthlyPlan";
import data_api from "@/store/data_api";
import { StripeElementCard } from "@vue-stripe/vue-stripe";
import { StripeCheckout } from "@vue-stripe/vue-stripe";

export default {
  name: "PaymentDetails",

  components: {
    Header,
    Footer,
    MonthlyPlan,
    StripeElementCard,
    StripeCheckout,
  },
  mounted() {
    this.create_payment();
    console.log("data is", this.$store.state.first_name);
    window.scrollTo(0, 0);
    window.addEventListener("resize", this.set_dims);

    //Tentatively
    let self = this;

    let elements = this.stripe.elements();
    this.card = elements.create("card");
    this.card.mount("#aio-card");
    this.card.on("change", this.card_change);
    document
      .querySelector(".stripe-form")
      .addEventListener("submit", self.checkout_submit);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.set_dims);
    console.log("Resize destroyed");
  },
  data() {
    this.publishableKey = process.env.VUE_APP_STRIPE_PK;

    return {
      card_information: "",
      name_on_card: "",
      country: "",
      region: "",
      address: "",
      stripe_secret: "",
      checkout_disabled: true,
      checkout_error: "",
      checkout_loading: false,
      card: null,
      current_width: window.innerWidth,
      current_height: window.innerHeight,
      purchase_loading: false,
      subscription: "",
      addressLine1: "",
      addressLine2: "",
      city: "",
      state: "",
      zipcode: "",
      manualAddress: false,

      //zendesk Endpoint
      zenEndpointUsers: "https://dorks.zendesk.com/api/v2/users",

      //from Stripe Checkout
      stripe: Stripe(process.env.VUE_APP_STRIPE_PK),
      pk: `${process.env.VUE_APP_STRIPE_PK}`,
      email: "",
    };
  },
  computed: {
    // form_active: function () {
    //   console.log(this.$store.getters.get_form_active);
    //   return this.$store.getters.get_form_active;
    // },

    is_mobile: function () {
      console.log(this.current_width, this.current_height);
      return this.current_width < 768;
    },
    // get_myself_form: function () {
    //   let purchase_form = this.$store.getters.get_purchase_form;
    //   this.first_name = purchase_form.first_name;
    //   this.last_name = purchase_form.last_name;
    //   this.email = purchase_form.email;
    // },
    // get_gift_form: function () {
    //   let gift_form = this.$store.getters.get_gift_form;
    //   this.gift_receiver_name = gift_form.to_name;
    //   this.gift_receiver_email = gift_form.to_email;
    //   this.gift_receiver_message = gift_form.to_message;
    // },

    load_form_data: function () {
      let form_active = this.$store.getters.get_form_active;
      if (form_active === 0) {
        let purchase_form = this.$store.getters.get_purchase_form;
        if (purchase_form.email) {
          this.email = purchase_form.email;
        }
        if (purchase_form.first_name.trim() && purchase_form.last_name.trim()) {
          this.name_on_card =
            purchase_form.first_name + " " + purchase_form.last_name;
        }
      } else if (form_active === 1) {
        let gift_form = this.$store.getters.get_gift_form;
      }
    },
    form_active: function () {
      console.log("does this get update or what");
      return this.$store.getters.get_form_active;
    },
  },
  methods: {
    toggleAddressForm: function () {
      this.manualAddress = true;
    },

    checkout_submit: async function (event) {
      this.checkout_loading = true;
      event.preventDefault();
      let form_active = this.$store.getters.get_form_active;
      // if form is purchase form
      if (form_active === 0) {
        let email = this.$store.getters.get_email;
        let self = this;

        // check if the user has already purchased a plan
        data_api.check_purchased(email).then((result) => {
          if (result.hasOwnProperty("result") && result.result) {
            self.checkout_loading = false;
            alert("You have already purchased dorks");
          } else {
            self.confirm_card_payment({ action: "purchase_dorks" });
          }
        });
        // if form is gift_form
      } else {
        let self = this;
        self.confirm_card_payment({ action: "gift_dorks" });
      }
    },

    confirm_card_payment: async function (payload = undefined) {
      let self = this;
      let form_active = this.$store.getters.get_form_active;
      self.stripe
        .confirmCardPayment(self.stripe_secret, {
          payment_method: { card: self.card },
        })
        .then(function (result) {
          console.log(result);
          if (result.error) {
            // Show error to your customer
            self.checkout_error = result.error.message;
          } else {
            result["action"] = payload["action"];
            result["name_on_card"] = self.name_on_card;
            result["email"] = self.email;

            data_api.store_successful_payment(result).then((data) => {
              console.log("checkout response", data);
              if (data.result) {
                self.$router.push(
                  form_active === 0
                    ? "/purchase/result/myself"
                    : "/purchase/result/gift"
                );
              } else if (data.error) {
                alert(data.error);
              }
            });
          }
        })
        .finally((s) => {
          self.checkout_loading = false;
        });
    },

    create_payment: async function () {
      let payment_secret = await data_api.create_payment("dorks_annual");
      this.stripe_secret = payment_secret.secret;

      // if(this.subscription == 'Yearly'){
      //   let payment_secret = await data_api.create_payment("dorks_annual");
      //   this.stripe_secret = payment_secret.secret;
      //   // console.log(this.stripe_secret)
      // }else if(this.subscription=="Monthly"){
      //      let payment_secret = await data_api.create_payment("dorks_monthly");
      //   this.stripe_secret = payment_secret.secret;
      // }else{
      //     alert("Please Select Subscription")
      // }
    },

    // create_payment : function(){

    // var response = fetch('/create/payment').then(function(response) {
    //   return response.json();
    // }).then(function(responseJson) {
    //   this.stripe_secret = responseJson.secret;
    //   // Call stripe.confirmCardPayment() with the client secret.
    // });

    // },

    card_change: function (event) {
      // Disable the Pay button if there are no card details in the Element
      this.checkout_disabled = event.empty;
      this.checkout_error = event.error ? event.error.message : "";
    },

    checkout: async function () {},

    makePayment: function () {
      //payment flow ...

      // To be changed to env
      const username = "kmarc9066@gmail.com";
      const password = "As123!@#";

      let name =
        this.$store.state.first_name + " " + this.$store.state.last_name;
      let email = this.$store.state.email;

      const token = Buffer.from(`${username}:${password}`, "utf8").toString(
        "base64"
      );
      const userData = {
        user: {
          email: email,
          name: name,
        },
      };
      this.axios
        .post(this.zenEndpointUsers, userData, {
          headers: {
            Authorization: `Basic ${token}`,
          },
        })
        .then(
          (response) => console.log(response),
          console.log('Added to Zendesk')
        )
        .catch((error) => {
          console.error("There was an error!", error);
        });
    },

    navigate_stripe_checkout: function () {
      let anchor_tag = document.createElement("a");
      anchor_tag.href = "https://buy.stripe.com/test_7sI5m31kVfAIbyE5kk";
      anchor_tag.setAttribute("target", "_blank");
      anchor_tag.click();
    },

    valid_email: function (email) {
      let email_re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return email_re.test(email);
    },

    validate_myself_form: function (myself_form) {
      let [valid, error_message] = [true, ""];
      if (myself_form.first_name.length === 0) {
        [valid, error_message] = [false, "First name is required"];
      } else if (myself_form.last_name.length === 0) {
        [valid, error_message] = [false, "Last name is required"];
      } else if (!this.valid_email(myself_form.email)) {
        [valid, error_message] = [false, "Please enter a valid email"];
      } else if (!myself_form.tos) {
        [valid, error_message] = [false, "Please accept terms of service"];
      }
      return [valid, error_message];
    },

    set_dims: function () {
      this.current_width = window.innerWidth;
      this.current_height = window.innerHeight;
    },
  },
};
</script>
