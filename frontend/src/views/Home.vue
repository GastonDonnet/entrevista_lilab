<template>
  <div class="home container mx-auto md:my-20">
    <div v-if="credits.length">
      <div class="flex flex-col items-center">
        <div
          v-for="(credit, i) in credits"
          :key="i"
          class="m-4 w-full md:w-1/2 bg-gray-5 shadow-xl"
        >
          <div
            class="text-2xl p-4 bg-gray-300"
            :class="{
              'bg-green-200': credit.ia_evaluation > 8,
              'bg-yellow-200':
                credit.ia_evaluation <= 8 && credit.ia_evaluation >= 5,
              'bg-red-200': credit.ia_evaluation < 5,
            }"
          >
            <div>Crédito</div>
            <div>USD {{ credit.amount }}</div>
          </div>
          <div class="p-8 flex flex-row">
            <div class="w-1/2 text-lg text-left">
              <div>Nombre:</div>
              <div>Deuda:</div>
              <div>Estado:</div>
              <div>Puntuación:</div>
              <div>Evaluación IA:</div>
            </div>
            <div class="w-1/2 text-lg text-left">
              <div>{{ credit.client.name }}</div>
              <div>{{ credit.client.total_debt }}</div>
              <div>{{ creditStates[credit.state] }}</div>
              <div
                :class="{
                  'text-green-500': credit.client.punctuation == 'B',
                  'text-yellow-500': credit.client.punctuation == 'R',
                  'text-red-500': credit.client.punctuation == 'M',
                }"
              >
                {{ clientPunctuations[credit.client.punctuation] }}
              </div>
              <div
                :class="{
                  'text-green-500': credit.ia_evaluation > 8,
                  'text-yellow-500':
                    credit.ia_evaluation <= 8 && credit.ia_evaluation >= 5,
                  'text-red-500': credit.ia_evaluation < 5,
                }"
              >
                {{ credit.ia_evaluation }}
              </div>
            </div>
          </div>
          <div class="p-8 flex flex-row border-t-2 border-gray-300">
            <button
              @click="updateCreditState(credit, 'A')"
              class="mx-4 p-4 w-1/2 bg-green-500 text-white font-semibold rounded-xl shadow-lg"
            >
              Aprobar
            </button>
            <button
              @click="updateCreditState(credit, 'NA')"
              class="mx-4 p-4 w-1/2 bg-red-500 text-white font-semibold rounded-xl shadow-lg"
            >
              Desaprobar
            </button>
          </div>
        </div>
      </div>
      <div class="flex flex-col">
        <div class="mx-auto flex flex-row w-full md:w-1/2">
          <button
            v-if="previousPage"
            @click="getCredits(previousPage)"
            class="p-4 w-5/12 mr-auto bg-gray-200 text-gray-500 font-semibold rounded-xl"
          >
            Anterior
          </button>
          <button
            v-if="nextPage"
            @click="getCredits(nextPage)"
            class="p-4 w-5/12 ml-auto bg-gray-200 text-gray-500 font-semibold rounded-xl"
          >
            Siguiente
          </button>
        </div>
        <div class="my-3 text-gray-400" v-if="totalPages">
          {{ page }} / {{ totalPages }}
        </div>
      </div>
    </div>
    <div v-else>No hay créditos menores a USD 50.000 por revisar</div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
  data() {
    return {
      credits: [],
      page: 1,
      nextPage: undefined,
      previousPage: undefined,
      totalPages: undefined,

      creditStates: {
        NR: "No revisado",
        A: "Aprobado",
        NA: "No aprobado",
      },
      clientPunctuations: {
        R: "Regular",
        B: "Bueno",
        M: "Malo",
      },
    };
  },

  methods: {
    async getCredits(page = 1) {
      try {
        this.page = page;
        const res = await this.$http.get(
          `credit?state=NR&amount__lte=50000&page=${this.page}`
        );
        this.credits = res.data.results;
        this.totalPages = res.data.count;

        if (res.data.next) this.nextPage = this.page + 1;
        else this.nextPage = undefined;

        if (res.data.previous) this.previousPage = this.page - 1;
        else this.previousPage = undefined;
      } catch (error) {
        console.log(error);
      }
    },

    async updateCreditState(credit, state) {
      try {
        console.log(credit.id, state);
        if (state != "NA" && state != "A") return;
        await this.$http.patch(`credit/${credit.id}/`, {
          state: state,
        });

        if (this.nextPage) this.getCredits(this.page);
        else if (this.previousePage) this.getCredits(this.previousePage);
        else this.getCredits(1);
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    this.getCredits();
  },
};
</script>
