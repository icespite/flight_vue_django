<template>
  <div class="app-container">
    <el-tabs type="border-card" @tab-click="handleClick">
      <el-tab-pane label="Location">
        <div>
          <el-table
            :data="locationlist"
            style="width: 100%"
          >
            <el-table-column
              prop="id"
              label="id"
            />
            <el-table-column label="省份">
              <template slot-scope="scope">
                <el-input
                  v-model="scope.row.name"
                  size="small"
                  placeholder="请输入内容"
                  @change="handleEdit(scope.$index, scope.row)"
                />
              </template>
            </el-table-column>
            <el-table-column
              label="操作"
            >
              <template slot-scope="scope">
                <!--                提醒是否确认修改-->
                <el-popconfirm
                  confirm-button-text="确认"
                  cancel-button-text="不用了"
                  icon="el-icon-info"
                  icon-color="red"
                  title="确定修改省份吗"
                  @onConfirm="madifylocation(scope.row.id,scope.row.name)"
                >
                  <el-button slot="reference" type="info" icon="el-icon-edit" size="small" />
                </el-popconfirm>
                <el-popconfirm
                  confirm-button-text="确认"
                  cancel-button-text="不用了"
                  icon="el-icon-error"
                  icon-color="red"
                  title="确定删除吗，这可能会造成不可预知的错误"
                  @onConfirm="delelocation(scope.row.id)"
                >
                  <el-button slot="reference" type="danger" icon="el-icon-delete" size="small" />
                </el-popconfirm>

              </template>
            </el-table-column>
          </el-table>
          <el-button
            type="success"
            style="float:right"
            icon="el-icon-circle-plus-outline"
            @click="dialogFlightFormVisible = true"
          />
          <el-button type="primary" style="float:right" icon="el-icon-refresh" @click="fetchAlllocation" />
        </div>
        <!--        嵌套添加表单-->
        <el-dialog title="添加location" :visible.sync="dialogFlightFormVisible">
          <el-form :model="flightform">
            <!--            <el-form-item label="id">-->
            <!--              <el-input v-model="flightform.id" autocomplete="off" />-->
            <!--            </el-form-item>-->
            <el-form-item label="省份">
              <el-input v-model="flightform.name" autocomplete="off" />
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFlightFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="addlocation">确 定</el-button>
          </div>
        </el-dialog>
        <!--        嵌套添加表单结束-->
      </el-tab-pane>
      <!--      第一分页结束-->
      <el-tab-pane label="Airline">
        <div>
          <el-table
            :data="airlinelist"
            style="width: 100%"
          >
            <el-table-column
              prop="id"
              label="id"
            />
            <el-table-column label="公司">
              <template slot-scope="scope">
                <el-input
                  v-model="scope.row.name"
                  size="small"
                  placeholder="请输入内容"
                  @change="handleEdit(scope.$index, scope.row)"
                />
              </template>
            </el-table-column>
            <el-table-column label="标识">
              <template slot-scope="scope">
                <el-input
                  v-model="scope.row.identifier"
                  size="small"
                  placeholder="请输入内容"
                  @change="handleEdit(scope.$index, scope.row)"
                />
              </template>
            </el-table-column>
            <el-table-column
              label="操作"
            >
              <template slot-scope="scope">
                <el-popconfirm
                  confirm-button-text="确认"
                  cancel-button-text="不用了"
                  icon="el-icon-info"
                  icon-color="red"
                  title="确定修改公司吗"
                  @onConfirm="madifyairline(scope.row.id,scope.row.name,scope.row.identifier)"
                >
                  <el-button slot="reference" type="info" icon="el-icon-edit" size="small" />
                </el-popconfirm>

                <el-popconfirm
                  confirm-button-text="确认"
                  cancel-button-text="不用了"
                  icon="el-icon-error"
                  icon-color="red"
                  title="确定删除吗，这可能会造成不可预知的错误"
                  @onConfirm="deleteairline(scope.row.id)"
                >
                  <el-button slot="reference" type="danger" icon="el-icon-delete" size="small" />
                </el-popconfirm>

              </template>
            </el-table-column>
          </el-table>
          <el-button
            type="success"
            style="float:right"
            icon="el-icon-circle-plus-outline"
            @click="airlinaddformvisable = true"
          />
          <!--        嵌套添加表单-->
          <el-dialog title="添加Airline" :visible.sync="airlinaddformvisable">
            <el-form :model="airlineform">
              <!--            <el-form-item label="id">-->
              <!--              <el-input v-model="flightform.id" autocomplete="off" />-->
              <!--            </el-form-item>-->
              <el-form-item label="公司">
                <el-input v-model="airlineform.name" autocomplete="off" />
              </el-form-item>
              <el-form-item label="标识">
                <el-input v-model="airlineform.identifier" autocomplete="off" />
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="airlinaddformvisable = false">取 消</el-button>
              <el-button type="primary" @click="addairline">确 定</el-button>
            </div>
          </el-dialog>
          <!--        嵌套添加表单结束-->
          <el-button type="primary" style="float:right" icon="el-icon-refresh" @click="fetchAllAirline" />
        </div>
      </el-tab-pane>
      <!--      <el-tab-pane label="角色管理">角色管理</el-tab-pane>-->
      <!--      <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>-->
    </el-tabs>
  </div>
</template>
<script>
import { getAllLocation, getAllAirline } from '../../api/user'
import { deleteairlinepost, modifyLocation, modifyAirline, addlocationpost, deletelocationpost, addairlinepost } from '../../api/manage'

export default {
  name: 'Index',
  data() {
    return {
      locationlist: [],
      airlinelist: [],
      airlinaddformvisable: false,
      dialogFlightFormVisible: false,
      airlineform: {
        name: '',
        identifier: ''
      },
      flightform: {
        id: '',
        name: ''
      }
    }
  },
  created() {
    this.fetchAlllocation()
  },
  methods: {
    fetchAlllocation() {
      getAllLocation().then(
        response => {
          this.locationlist = response.data.data
        }
      )
    },
    fetchAllAirline() {
      getAllAirline().then(
        response => {
          this.airlinelist = response.data
        }
      )
    },
    handleClick(tab, event) {
      console.log(tab, event)
      if (tab.label === 'Location') {
        this.fetchAlllocation()
      }
      if (tab.label === 'Airline') {
        this.fetchAllAirline()
      }
    },
    open(title = '标题', msg = '提示') {
      this.$notify({
        title: title,
        message: msg,
        type: 'success'
      })
    },
    madifylocation(id, name) {
      modifyLocation(id, name).then(
        response => {
          if (response.code === 20000) {
            this.open('success', '更新成功')
          }
        }
      )
    },
    addlocation() {
      this.dialogFlightFormVisible = false
      addlocationpost(this.flightform.name).then(response => {
        this.dialogFlightFormVisible = false
        this.open('success', '添加成功')
        this.fetchAlllocation()
      })
    },
    madifyairline(id, name, identify) {
      modifyAirline(id, name, identify).then(
        response => {
          if (response.code === 20000) {
            this.open('success', '更新成功')
            this.fetchAllAirline()
          }
        }
      )
    },
    delelocation(id) {
      deletelocationpost(id).then(res => {
        if (res.code === 20000) {
          this.open('success', '删除成功')
          this.fetchAlllocation()
        }
      })
    },
    deleteairline(id) {
      deleteairlinepost(id).then(res => {
        if (res.code === 20000) {
          this.open('success', '删除成功')
          this.fetchAllAirline()
        }
      })
    },
    addairline() {
      addairlinepost(this.airlineform.name, this.airlineform.identifier).then(res => {
        if (res.code === 20000) {
          this.airlinaddformvisable = false
          this.open('success', '添加Airline成功')
          this.fetchAllAirline()
        }
      })
    }

  }

}
</script>

<style scoped>

</style>
