<template>
  <div class="dashboard-container">

    <el-row :gutter="20">
      <el-col :span="16">
        <div class="grid-content bg-purple">

          <el-card shadow="always" style="width: 120px; background: #979A9A ">
            Inform
          </el-card>

          <template v-if="msglist">
            <el-table
              :data="msglist"
              style="width: 100%"
              :default-sort="{prop: 'haveConfirm'}"
            >
              <!--              <el-table-column-->
              <!--                prop="id"-->
              <!--                label="序号"-->
              <!--                width="180"-->
              <!--              />-->
              <el-table-column
                prop="time"
                label="日期"
                width="180"
              />
              <el-table-column
                prop="msg"
                label="内容"
                width="280"
              />
              <el-table-column
                prop="haveConfirm"
                label="状态"
              >
                <template slot-scope="scope">
                  <el-tag v-if="!scope.row.haveConfirm" type="danger">未确认</el-tag>
                  <el-tag v-else type="info">已确认</el-tag>
                </template>
              </el-table-column>
              <el-table-column>
                <template slot-scope="scope">
                  <el-button v-if="!scope.row.haveConfirm" style="background: #45B39D" @click="confirm(scope.row.id)">确认</el-button>
                </template>
              </el-table-column>
            </el-table>
          </template>

        </div>
      </el-col>

      <el-col :span="8">

        <el-card shadow="hover" style="background: #28B463">
          name: {{ name }}
        </el-card>
        <el-card shadow="hover" style="background: #3498DB ">
          roles: <span v-for="role in roles" :key="role">{{ role }}</span>
        </el-card>
      </el-col>
    </el-row>

  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { getInform, cofirmInform } from '../../api/user'

export default {
  name: 'Dashboard',
  data() {
    return {
      msglist: null

    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {
    this.fetchMsg()
  },
  methods: {
    fetchMsg(button) {
      getInform().then(response => {
        this.msglist = response.data.item
        if (button === 'tishi') {
          this.open('success', '更新成功')
        }
      })
    },
    open(title = '标题', msg = '提示') {
      this.$notify({
        title: title,
        message: msg,
        type: 'success'
      })
    },
    confirm(data) {
      cofirmInform(data).then(
        response => {
          if (response.code === 20000) {
            this.open('success', '确认成功')
          }
          this.fetchMsg()
        }
      )
    }
  }
}
</script>

<style lang="scss" scoped>
  .dashboard {
    &-container {
      margin: 30px;
    }

    &-text {
      font-size: 30px;
      line-height: 46px;
    }
  }
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    /*background: #d3dce6;*/
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
