<template>
  <div class="stripe-checkout">
    <!--        <img src="https://stripe-camo.global.ssl.fastly.net/82a77f27e4aa557142bf33e89ccbdd1acbe7f830129cefe65c44e248ad1ea0ce/68747470733a2f2f66696c65732e7374726970652e636f6d2f66696c65732f4d44423859574e6a64463878536b56535530354d5257397663545a6b5558687666475a666447567a6446394853464e745447354c64474a4b63565a56616d5a4957446858516b593361444130303131366e36787237" alt="">-->

    <Header></Header>
    <div class="purchase">
      <row :gutter="12">
        <column :xs="12" :md="4" :lg="3"></column>
        <column :xs="12" :md="4" :lg="3">
          <b-col cols="">
            <div class="purchase-title-container">
              <div class="content-title">Purchase Dorks</div>
              <div class="content-text">
                This is a body of text where we talk about the price, what you
                get and how cool Dorks really is and maybe a little about buying
                for others too.
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

            <div class="main-container">
              <form class="stripe-form">
                <div class="form-group">
                  <!--<label for="checkout_email">Email</label>-->
                  <input
                    v-model="email"
                    :disabled="form_active === 0"
                    id="checkout_email"
                    type="hidden"
                    placeholder="Enter email"
                    class="form-control"
                  />
                </div>

                <div class="form-group">
                  <div>
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
                </div>

                <div class="form-group">
                  <div>
                    <label for="checkout_name">Name on card*</label>
                    <input
                      v-model="name_on_card"
                      id="checkout_name"
                      type="text"
                      placeholder="Name as it appears"
                      class="form-control"
                    />
                  </div>
                </div>

                <div class="basic-addr-form" v-if="manualAddress == false">
                  <div>
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
              </form>
            </div>
          </b-col></column
        >
        <column :xs="12" :md="4" :lg="3"></column>
      </row>
    </div>

    {{ load_form_data }}
    <div class="purchase">
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
    
  </div>
</template>

<script>
import { StripeCheckout } from "@vue-stripe/vue-stripe";
import { StripeElementCard } from "@vue-stripe/vue-stripe";
import Header from "../components/Header";
import data_api from "@/store/data_api";
import Footer from "../components/Footer.vue";

export default {
  components: {
    StripeCheckout,
    StripeElementCard,
    Header,
    Footer,
  },

  data() {
    return {
      stripe: Stripe(process.env.VUE_APP_STRIPE_PK),
      pk: `${process.env.VUE_APP_STRIPE_PK}`,
      email: "",
      name_on_card: "",
      stripe_secret: "",
      checkout_disabled: true,
      checkout_error: "",
      checkout_loading: false,
      card: null,
      //zendesk Endpoint
      zenEndpointUsers: "https://dorks.zendesk.com/api/v2/users",
    };
  },
  mounted() {
       window.scrollTo(0, 0);
        window.addEventListener('resize', this.set_dims);
    let self = this;
    this.create_payment();
    let elements = this.stripe.elements();
    this.card = elements.create("card");
    this.card.mount("#aio-card");
    this.card.on("change", this.card_change);
    document
      .querySelector(".stripe-form")
      .addEventListener("submit", self.checkout_submit);
  },

   beforeDestroy() {
        window.removeEventListener('resize', this.set_dims);
        console.log("Resize destroyed");
    },

  methods: {
    checkout_submit: async function (event) {
      this.checkout_loading = true;
      this.sendToZen();
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
      // console.log(this.stripe_secret)
      
    },

    sendToZen: function () {

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

    card_change: function (event) {
      // Disable the Pay button if there are no card details in the Element
      this.checkout_disabled = event.empty;
      this.checkout_error = event.error ? event.error.message : "";
    },

     set_dims: function() {
            this.current_width = window.innerWidth;
            this.current_height = window.innerHeight;
        },

    checkout: async function () {},
  },

  computed: {
    is_mobile: function () {
      console.log(this.current_width, this.current_height);
      return this.current_width < 768;
    },

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
};
</script>

<style scoped>
input[type="text"] {
  height: auto;
  border-radius: 10px;
  width: 100%;
  border: 1px solid;
  padding-top: 15px;
  padding-bottom: 15px;
  margin-top: 15px;
}
</style>